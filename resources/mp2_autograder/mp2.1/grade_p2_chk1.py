#!/usr/bin/env python

# Notes:
# MP2 Checkpoint 1 autograder which is based on Checkpoint 2 autograder
# This script only runs in Linux
# Requires Selenium (pip install selenium) and MySQLdb (pip install mysqldb)
# before running this script, make sure you create user grader0 and grader for MySQL

import atexit
import sys
import os
import os.path
import csv
import time
import re
import subprocess
import signal

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, NoAlertPresentException 
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from common_grading import get_gui_check_grade, get_gui_grade
from multiprocessing import Process, Array

import MySQLdb as mdb

#GLOBAL VARIABLES
bungle_url = "http://127.0.0.1:8080"
browser = webdriver.Firefox() # Get new local session of firefox

def grade_filename(i):
    return os.path.join(os.path.abspath(os.path.curdir),
                        'mp2_chk1_grades_%03d.csv' % i)

# Select file to write grades
csv_file_handle = None
for i in range(1000):
    if not os.path.exists(grade_filename(i)):
        csv_file_handle = open(grade_filename(i), 'wb')
        grade_handle = csv.writer(csv_file_handle)
        break

def close_browser():
    try:
        browser.close()
    except:
        pass

atexit.register(close_browser)

class GradeProcess(object):
    def __init__(self, path, server, grades, partners):
        self.path = path
        self.server = server
        self.grades = grades
        self.partners = partners

    def run(self):
        grades = self.grades
        path = self.path
        partners = self.partners

        grades.extend(grade_prep(path))
        grades.extend(grade_filter(path))
        grades.extend(grade_tokval(path))
        output_grades(partners, grades)

        #send signal to server so that server can quit
        os.kill(self.server, signal.SIGINT)

class ServerProcess(object):
    def __init__(self, path):
        self.path = path

    def run(self):
        try:
            path = self.path
            os.chdir(path+'/bungle')
            p = subprocess.Popen(['python', 'project2.py'])
            p.wait()
        except KeyboardInterrupt:
            p.kill()
            os.system('fuser -k 8080/tcp')
            sleep()

def process(path, name):
    p = os.path.normpath(os.path.join(path, 'partners.txt'))
    if os.path.exists(p):
        partners = extract(p).replace('\r','').replace('\n','-')
        if partners == '':
            partners = name
        print partners
    else:
        partners = name

    grades = []
    grades.extend(grade_script(path, name))
    
    s = ServerProcess(path)   
    p1 = Process(target=s.run)
    p1.start()
    g = GradeProcess(path, p1.pid, grades, partners)
    p2 = Process(target=g.run)
    p2.start()
    p1.join()
    p2.join()    

def exec_sql_file(cursor, sql_file):
    """ a code which runs sql script (from stackoverflow) """

    print "\n[INFO] Executing SQL script file: '%s'" % (sql_file)
    statement = ""

    for line in open(sql_file):
        if re.match(r'--', line):  # ignore sql comment lines
            continue
        if not re.search(r'[^-;]+;', line):  # keep appending lines that don't end in ';'
            statement = statement + line
        else:  # when you get a line ending in ';' then exec statement and reset for next statement
            statement = statement + line
            try:
                cursor.execute(statement)
            except:
                return False
            statement = ""

    return True 

def grade_script(path, name):
    """ grader for 2.1.2 """

    print '== Grading 2.1.2'
    pt = 0
    comment = ""
    grade = []

    p1 = os.path.normpath(os.path.join(path, '2.1.2.txt'))
    print 'Grading "%s"' % p1
    if os.path.exists(p1) and extract(p1) != '':
        try:            
            #clean up database before grading
            #db_0 = mdb.connect(host="localhost",
            #                   user="grader0",
            #                   passwd="checkpoint1",
            #                   db="project2")
            #cur = db_0.cursor()
            #exec_sql_file(cur, 'script1.txt')
            
            #run student's sql script
            db_rw = mdb.connect(host="localhost",
                                user="grader",
                                passwd="checkpoint1",
                                db="project2")
            cur = db_rw.cursor()
            #result = exec_sql_file(cur, p1)
            #if result is False:
            #    raw_input("Manually run script for "+name)

            #see if tables are there
            cur.execute("show tables;")
            rows = cur.fetchall();
            if set(rows) == set([('history',), ('users',)]):
                pt += 2                
            else:
                comment += "table name incorrect;"

            #see if columns for history is correct
            cur.execute("show columns from history")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == 'id':
                    if (row[1] == 'int(11)' and 
                        row[2] == 'NO' and 
                        row[3] == 'PRI' and 
                        row[5] == 'auto_increment'):
                        pt += 0.5
                    else:
                        comment += "history's id column incorrect;"
                elif row[0] == 'user_id':
                    if (row[1] == 'int(11)' and
                        row[2] == 'NO'):
                        pt += 0.5
                    else:
                        comment += "history's user_id column incorrect;"
                elif row[0] == 'query':
                    if (row[1] == 'varchar(2048)' and 
                        row[2] == 'NO'):
                        pt += 0.5
                    else:
                        comment += "history's query column incorrect;"

            #see if columns for user is correct        
            cur.execute("show columns from users")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == 'id':
                    if (row[1] == 'int(11)' and 
                        row[2] == 'NO' and 
                        row[3] == 'PRI' and 
                        row[5] == 'auto_increment'):
                        pt += 0.4
                    else:
                        comment += 'column id for users incorrect;'
                elif row[0] == 'username':
                    if row[1] == 'varchar(32)' and row[2] == 'NO':
                        pt += 0.4
                    else:
                        comment += "column username incorrect for users;"
                elif row[0] == 'password':
                    if (row[1] == 'varchar(32)' and 
                        row[2] == 'NO'):
                        pt += 0.4
                    else:
                        comment += "column password incorrect for users;"
                elif row[0] == 'passwordhash':
                    if (row[1] == 'tinyblob' and 
                        row[2] == 'NO'):
                        pt += 0.3
                    else: 
                        comment += "column passwordhash incorrect for users;"

            pt = round(pt, 1)
            grade.append((pt, comment))

        except:
            grade.append((0, "SQL ERROR (table/column name incorrect)"))
    else:
        grade.append((0, "no submission"))
        
    assert len(grade) == 1
    return grade

def grade_prep(path):
    """ grader for 2.1.3 """

    print '== Grading 2.1.3'
    grade = []
    browser.get("http://127.0.0.1:8080")
    browser.delete_all_cookies()
    
    #check if account creation and login works or not (2 pts)
    browser.get("http://127.0.0.1:8080")
    can_cont = False
    try:
        username = browser.find_element_by_id("username")
        userpass = browser.find_element_by_id("userpass")
        na_button = browser.find_element_by_id("new-account-btn")
        username.send_keys("newaccount")
        userpass.send_keys("helloworld")
        na_button.click()
        sleep()
        if (browser.find_element_by_id('logged-in-user').text
                == 'newaccount'):
            browser.find_element_by_id("log-out-btn").click()
            can_cont = True
            grade.append((2.0,''))
        else:
            can_cont = True
            grade.append((0.5,'account authentication failed'))
            browser.find_element_by_id("log-out-btn").click()
    except NoSuchElementException:
            grade.append((0,'account creation failed'))

    #SQL injection (1 pt)
    if can_cont is True:
        username = browser.find_element_by_id("username")
        userpass = browser.find_element_by_id("userpass")
        login = browser.find_element_by_id("log-in-btn")
        username.send_keys("newaccount")
        userpass.send_keys("\" OR 1=1; -- ")
        login.click()
        sleep()
        try:
            browser.find_element_by_id('logged-in-user')
            grade.append((0,'SQL injection succeeded'))
            browser.find_element_by_id("log-out-btn").click()
        except NoSuchElementException:
            grade.append((1.0,''))
            browser.get("http://127.0.0.1:8080")
    else:
        grade.append((0.0,'cant test SQL injection'))

    if can_cont is True:
        try:
            #check if validation is correct or not (1 pt)
            username = browser.find_element_by_id("username")
            userpass = browser.find_element_by_id("userpass")
            login = browser.find_element_by_id("log-in-btn")
            username.send_keys("newaccount")
            userpass.send_keys("worldhello")
            login.click()
            sleep()
            browser.find_element_by_id('logged-in-user')
            grade.append((0, 'logged in with wrong password'))
        except NoSuchElementException:
            grade.append((1.0,''))
            browser.get("http://127.0.0.1:8080")
    
        
        #check if history is stored and displayed correctly (1 pt)        
        try:
            #lets fill up history for another account before doing this    
            username = browser.find_element_by_id("username")
            userpass = browser.find_element_by_id("userpass")
            username.send_keys("historytest")
            userpass.send_keys("historytest")
            browser.find_element_by_id("new-account-btn").click()
            sleep()
            browser.get("http://127.0.0.1:8080/search?q=aaa")
            browser.get("http://127.0.0.1:8080/search?q=bbb")
            browser.get("http://127.0.0.1:8080/search?q=ccc")
            browser.find_element_by_id("log-out-btn").click() #done, logout

            username = browser.find_element_by_id("username")
            userpass = browser.find_element_by_id("userpass")
            username.send_keys("newaccount")
            userpass.send_keys("helloworld")
            browser.find_element_by_id("log-in-btn").click()
            sleep()

            for x in range(0, 17):
                browser.get("http://127.0.0.1:8080/search?q="+str(x))
                if x == 16:
                    browser.get("http://127.0.0.1:8080/search?q="+str(x))
            try:
                browser.find_element_by_xpath("//a[@href='search?q=0']")
                grade.append((0.0,'failed to display last 15 searches'))
            except:
                grade.append((1.0,''))
            browser.find_element_by_id('log-out-btn').click()
        except NoSuchElementException: 
            grade.append((0,'search test failed'))
    else:
        grade.append((0,''))
        grade.append((0,''))

    assert len(grade) == 4
    return grade

def grade_filter(path):
    """ grader for 2.1.4 """

    print '== Grading 2.1.4'
    grade = []
    pt = 0
    comment = ''
    
    try:
        browser.get("http://127.0.0.1:8080")
        browser.delete_all_cookies()
        browser.get("http://127.0.0.1:8080/?xssdefense=1")
        query = browser.find_element_by_id('query')
        search_btn = browser.find_element_by_id('search-btn')
        query.send_keys('<script>alert()</script>') #check if XSS works or not (3 pts)
        search_btn.click()

        try:
            alert = browser.switch_to_alert()
            alert.accept()
            comment = 'XSS defense failed'
        except NoAlertPresentException:
            pt += 3.0
            query = browser.find_element_by_id('query-lbl')
            
            #check if correct filter is used or not (2 pts)
            if ('&lt' in query.text and 
                ('&rt' in query.text or 
                '&gt' in query.text)):
                pt += 2.0
            else:
                comment = "Incorrect filter"
    except:
        comment = '2.1.4 not implemented'

    grade.append((pt, comment))
    assert len(grade) == 1
    return grade

def grade_tokval(path):
    """ grader for 2.1.5 """

    print '== Grading 2.1.5'
    grade = []

    try:
        # Load bungle, clear cookies
        browser.get("http://127.0.0.1:8080/?csrfdefense=1")
        browser.delete_all_cookies()
        browser.get("http://127.0.0.1:8080/?csrfdefense=1")

        # Check cookies (3 pts)
        token1 = browser.get_cookie('csrf_token')
        assert token1 != None
        browser.delete_all_cookies()
        browser.get("http://127.0.0.1:8080/?csrfdefense=1")

        token2 = browser.get_cookie('csrf_token')
        assert token2 != None
        assert token1 != token2
        grade.append((3.0, ""))
    except:
        grade.append((0, "Token validation failed"))

    # Check if login succeeds or not (2 pts)
    try:
        username = browser.find_element_by_id("username")
        userpass = browser.find_element_by_id("userpass")
        login = browser.find_element_by_id("log-in-btn")
        username.send_keys("newaccount")
        userpass.send_keys("helloworld")
        login.click()
        sleep()
        browser.find_element_by_id('logged-in-user')
        grade.append((2.0,''))
    except NoSuchElementException:
        grade.append((0,'authentication failed'))

    assert len(grade) == 2
    return grade

def sleep(t=0.8):
    time.sleep(t)

def extract(path):
    with open(path) as f:
        return f.read().strip()


def output_grades(name, grades):
    grade_list = [name] + [item for tup in grades for item in tup]
    grade_handle.writerow(grade_list)
    csv_file_handle.flush()
    print grade_list


def project_dirs(svn_root):
    path_list = []
    with open(svn_root+'_rosters/temp.txt') as f:
        for line in f:
            path_list.append((svn_root+line.strip()+'/mp2',line.strip()))
    return path_list

def main():
    print sys.argv

    #TODO: change this so that this corresponds to your svn directory
    svn_root = "/home/hyunbinl/sp16-ece422/"

    # Check if a target is specified
    if len(sys.argv) == 3 and sys.argv[1] == '-t':
        full = svn_root+sys.argv[2]+"/mp2"
        print "Begin grading target:", sys.argv[2]
        process(full,sys.argv[2])
        sys.exit(0)

    # Do a normal resumption
    if len(sys.argv) > 1:
        begin_grading = False
    else:
        begin_grading = True

    for i, full in enumerate(project_dirs(svn_root)):
        print full
        if begin_grading:
            print '==== Grading "%s"' % full[1]
            process(full[0], full[1])
        else:
            if os.path.samefile(p, sys.argv[1]):
                # Found last graded file file, resume grading
                begin_grading = True
                print "Found ", p, "; You have graded:", i, \
                    "so far, keep going"
                print "-----Commence grading-----"

if __name__ == '__main__':
    main()
