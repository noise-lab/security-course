#!/usr/bin/env python

# Notes:
# This script only runs in Linux
# Requires Selenium (pip install selenium)
# SQL inject grading is completely automated, except for sql3
# CSRF grading is completely automated (w/ Selenium), except csrf2
# XSS grading is done by hand and input in GUI dialogs

import atexit
import sys
import os
import os.path
import traceback
import hashlib
import multiprocessing
import urllib
import urllib2
import csv
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from common_grading import get_gui_check_grade, get_gui_grade
import log_listen

#URL TO BUNGLE
bungle_url = "http://bungle.cs461.cs.illinois.edu"

def grade_filename(i):
    return os.path.join(os.path.abspath(os.path.curdir),
                        'mp2_grades_%03d.csv' % i)

# Select file to write grades
csv_file_handle = None
for i in range(1000):
    if not os.path.exists(grade_filename(i)):
        csv_file_handle = open(grade_filename(i), 'wb')
        grade_handle = csv.writer(csv_file_handle)
        break

browser = webdriver.Firefox() # Get new local session of firefox


def close_browser():
    try:
        browser.close()
    except:
        pass


atexit.register(close_browser)

def process(path, name):
    p = os.path.normpath(os.path.join(path, 'partners.txt'))
    if os.path.exists(p):
        partners = extract(p).replace('\r','').replace('\n','-')
        print partners
    #else:
        #partners = name

    grades = []
    grades.extend(grade_sql(name,path))
    grades.extend(grade_csrf(path))
    grades.extend(grade_multivac(path))
    grades.extend(grade_xss(path))

    # Add column for penalties
    grades.append((0, 'On time'))


    output_grades(partners, grades)

def grade_xss(path):
    """
    Grading criteria
    ================
    Grade scheme:
        Stealth
            +3 URL
            +3 Search History
        Persistence
            +3 Following link
            +3 Forward
            +3 Back
        Spying
            +3 log login/logout events
            +3 log nav events
        Other
            -3 Repeated input

    For xss_payload:
        +4 Submitted
    """

    browser.delete_all_cookies()
    print '== Grading XSS'
    xss_grades = []
    prev_input = set()

    file_list = ['2.2.3.2_payload.html', '2.2.3.2.txt', '2.2.3.3.txt',
                 '2.2.3.4.txt', '2.2.3.5.txt', '2.2.3.6.txt']
    for i, file in enumerate(file_list):
        p1 = os.path.normpath(os.path.join(path, file))
        print 'Grading "%s"' % p1
        if not os.path.exists(p1):
            print 'Did not find file "%s"' % file
            xss_grades.append((0, "No file submitted"))
            continue

        if extract(p1) == '':
            xss_grades.append((0, "no submission"))
            continue

        if 'payload' in file:
            # Give points if submitted
            if extract(p1) != '':
                (grade, comment) = (4, '')
            else:
                (grade, comment) = (0, 'no submission')

        else:
            xss = extract(p1)
            print '\n'+xss+'\n'
            listener = multiprocessing.Process(target=log_listen.run_server)
            listener.start()
            browser.get(xss)
            if file == '2.2.3.2.txt':
                # Do full grading
                (grade, comment) = get_gui_check_grade(file,
                        ['Stealth: URL hiding', 'Stealth: search history',
                         'Persistence: Follow link', 'Persistence: back button',
                         'Persistence: forward button', 'Spying: login/logout events', 
                         'Spying: nav events'])
                #give 3 points for each category
                (grade, comment) = (grade * 3, comment)
            else:
                # For xss[1-4].txt, do minimal grading (probably works fully or not)
                (grade, comment) = get_gui_grade(file, 5)

            listener.terminate()

        # Ensure grade is >= 0
        xss_grades.append((max(grade, 0), comment))

    assert len(xss_grades) == 6
    return xss_grades

def grade_multivac(path):
    print '== Grading Multivac'
    expected_answer = "ece.illinois.edu"
    p = os.path.normpath(os.path.join(path, '2.2.3.1.txt'))
    url = extract(p)
    if url == '':
        return [(0,'no submission')]
    
    try:
        browser.get(url);
        sleep()
        elem =  browser.find_element_by_link_text('Click me')
        if(elem.get_attribute('href').find(expected_answer) >=0):
            return [(5,'passed')]
        else:
            elem.click()
            sleep()
            if(browser.current_url.find(expected_answer) >=0):
                return [(5,'passed')]
            return [(0,'wrong redirection')]
    except Exception:
        return [(0,'Click me element not found')]

def grade_sql(netid,path):
    print '== Grading SQL'
    sql_grades = []
    prev_pw = set()
    file_list = ['2.2.1.1.txt', '2.2.1.2.txt', '2.2.1.3.tar.gz']
    url_base = bungle_url+'/sqlinject'
    url_list = [url_base + str(x) + '/checklogin.php' for x in range(0,len(file_list))]

    max_credit = 5
    max_credit_2 = 10

    for i, url in enumerate(url_list):
        p1 = os.path.normpath(os.path.join(path, file_list[i]))
        print 'Grading "%s"' % p1
        if os.path.exists(p1):
            try:
                on_sql2 = (file_list[i] == '2.2.1.3.tar.gz')
                if on_sql2:
                    sql2_txt = os.path.join(path, '2.2.1.3.txt')
                    pw = get_password(sql2_txt)
                else:
                    pw = get_password(p1)

                prev_used_multiplier = 1
                prev_used_message = ""

                if 'Login successful!' in send_injection(url, pw):
                    if on_sql2:
                        sql_grades.append((max_credit_2 * prev_used_multiplier,
                                           'Success' + prev_used_message))
                    else:
                        sql_grades.append((max_credit * prev_used_multiplier,
                                           'Success' + prev_used_message))
                    prev_pw.add(pw)
                else:
                    # Don't deduct multiplier if the test case failed...
                    sql_grades.append((1, 'Did not succeed'))

            except IOError as e:
                print e
                print file_list[i], 1, "failed"
                sql_grades.append((-1000, 'Failure issue... take a look'))
        else:
            print "  --> File does not exist"
            sql_grades.append((0, "Does not exist"))

    # Grade SQL 3
    p1 = os.path.join(path, '2.2.1.4.txt')
    print 'Grading "%s"' % p1
    sql_grades.append(sql3_grade(netid,p1))

    assert(len(sql_grades) == 4)
    return sql_grades

def sleep(t=0.8):
    time.sleep(t)

def grade_csrf(path):
    print '== Grading CSRF'
    csrf_grades = []
    prev_input = set()
    file_list = ['2.2.2.1.html', '2.2.2.2.html']
    main_page = [bungle_url+'/?csrfdefense=0&xssdefense=5', bungle_url+'/?csrfdefense=1&xssdefense=0']
    for i, file in enumerate(file_list):
        p1 = os.path.normpath(os.path.join(path, file_list[i]))
        print 'Grading "%s"' % p1
        if os.path.exists(p1) and extract(p1) != '':
            try:
                # Load bungle, clear cookies
                browser.get(main_page[i])
                sleep()
                browser.delete_all_cookies()
                browser.get(main_page[i])
                sleep()
                assert "Bungle" in browser.title

                # Load CSRF page
                csrf_url = "file://" + os.path.abspath(p1)
                browser.get(csrf_url)
                sleep()

                # Check that CSRF is silent
                try:
                    if csrf_url != browser.current_url:
                        csrf_grades.append((0,
                                'CSRF page redirected to another page'))
                        continue
                except UnexpectedAlertPresentException:
                    csrf_grades.append((0,
                            'Unexpected alert box'))
                    continue
                sleep()

                # Load bungle again
                browser.get(main_page[i])
                sleep()

                # Check cookies
                cd_cookie = browser.get_cookie('csrfdefense')
                assert cd_cookie != None
                if cd_cookie['value'] != str(i):
                    csrf_grades.append((0, 'Wrong csrfdefense level'))
                    continue

                # Check logged in user
                try:
                    if (browser.find_element_by_id('logged-in-user').text
                            != 'attacker'):
                        csrf_grades.append((0, 'Logged as wrong user'))
                        continue
                except NoSuchElementException:
                    csrf_grades.append((0, 'Not logged in'))
                    continue

                csrf_grades.append((10, ''))

                continue
            except:
                # Unexpected error
                print traceback.format_exc()
                browser.close()
                sys.exit(1)
        else:
            csrf_grades.append((0, "no submission"))
            continue

    assert len(csrf_grades) == 2
    return csrf_grades

def sql3_grade(netid, fp):
    grade = 0
    comment = ""
    line_ctr = 0
    
    if os.path.exists(fp):
        with open(fp, 'r') as f:
            for line in f:
                if line_ctr == 0:
                    if (line.strip() == "proj2_inject3"):
                        grade += 1
                    else:
                        comment += "database name incorrect; "
                if line_ctr == 1:
                    if (line.strip() == "5.5.47-0ubuntu0.14.04.1"):
                        grade += 1
                    else:
                        comment += "server version incorrect; "
                if line_ctr == 2:
                    table_names = line.strip().split(',')
                    table_names = [name.rstrip().lstrip() for name in table_names]
                    sol = ['foo','HINT','inject3_users','SECRET']
                    if set(sol) == set(table_names):
                        grade += 4                    
                    else:
                        comment += "table name incorrect; "
                if line_ctr == 3:
                    secret = ['alpha',
                    'brabo',
                    'charlie',
                    'delta',
                    'echo',
                    'foxtrot',
                    'golf',
                    'hotel',
                    'india',
                    'juliett']
                    md5 = hashlib.md5(netid).hexdigest()
                    sol = secret[int(md5,16)%10]
                    if sol == line.strip():
                        grade += 4
                    else:
                        comment += "secret string incorrect for "+netid
                line_ctr += 1

    return (grade, comment)

def send_injection(url, password):
    print url, password
    values = {'username': 'victim',
              'password': password}

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    return response.read()

def get_password(path):
    text = extract(path)
    index = text.find('password=')
    encoded_password = text[index + 9:]
    try:
        return urllib.unquote(encoded_password).decode('utf8')
    except:
        return False


def get_password_from_text(text):
    index = text.find('password=')
    encoded_password = text[index + 9:]
    try:
        return urllib.unquote(encoded_password).decode('utf8')
    except:
        return False


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
    #TODO: change this so that you have list_x.txt
    with open(svn_root+'_class/_private/mp2_autograder/list_1.txt') as f:
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
