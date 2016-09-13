#!/usr/bin/env python

import re
import sys
import os
import os.path
import subprocess
import shutil
import time
import signal
from datetime import datetime

error = 0
FULL_CREDIT = 4
ROUNDS = 100

       
def process(proj_dir, netid):
    print "grading %s" %(netid)
    if not os.path.exists(proj_dir):
        return -1

    os.chdir(proj_dir)

    copy_files(proj_dir)
    set_cookie(netid)
    subprocess.check_output(['make', 'clean'])
    try:
        subprocess.check_output(["sudo", "make"])
    except:
        global error
        error = 1

    grades = []
    for i in range(6):
        if error == 1:
            comment ="cannot compile"
            grade = 0
        else:
            grade = grade_app(proj_dir, i)
            if isinstance(grade,int):
                comment =""
            else:
                comment = grade
                grade = 0
        grades.append((grade, comment))

    global error
    error = 0

    try:
        kill_code = subprocess.check_call(["pkill", "-f", "/bin/sh"])
        kill_code = subprocess.check_call(["pkill", '-f', '/bin//sh'])
        kill_code = subprocess.check_call(["pkill", '-f', 'sudo /bin/bash'])
    except:
        pass

    grade_list = [item for tup in grades for item in tup]
    print netid +","+ str(grade_list).strip('[]')
    return str(grade_list).strip('[]')+'\n'

def run_shell_test(shell_string, wait_period=.5):
    try:
        proc = subprocess.Popen([shell_string], stdout=subprocess.PIPE, shell=True,preexec_fn=os.setsid)
        time.sleep(wait_period)
        retcode = proc.poll()
        if retcode is None:
            # this indicates process is still running ie. shell is executing
            os.killpg(proc.pid, signal.SIGTERM)

            return FULL_CREDIT
    except KeyboardInterrupt:
        return FULL_CREDIT
    except Exception as e:
        print "Exception occured:", e
        return "An error occured"

    # This indicates the program exited with no problems
    return "Shell was not running"

def grade_app(proj_dir, num):
    tar = "1.1.%d" % (num)

    sol = "1.1.%d.S" % (num)

    if num == 0:
        sol = "1.1.1_addr.txt"
    if num == 1:
        sol = "1.1.1_eax.txt"
        
    if not os.path.exists(sol):
        return "no solution file"

    if num <= 1:
        g=open(sol)
        ans = g.readline().lstrip('0').lstrip('x').lstrip('0').strip()
        if num == 0:
            stdout = "8048f20"
        elif num == 1:
            stdout = subprocess.Popen(['./%s' % (tar)], stdout=subprocess.PIPE, shell=True).communicate()[0].strip()
        if stdout in ans:
            return 2
        else:
            return "Expected %s. Got %s." % (stdout,ans)
    

    elif num <= 4:
        stdout = subprocess.Popen(['./%s' % (tar)], stdout=subprocess.PIPE, shell=True).communicate()[0].strip()
        
        if stdout == "Good job!":
            return FULL_CREDIT
        else:
            return "Got %s." % (stdout)

    elif num == 5:
        shellString = "./%s" % (tar)
        print shellString
        return run_shell_test(shellString)
 
    else:
        print "Invalid question number given to grader"
        return 10000

# copy file from our target_dir to student's proj_dir
# so I guess we'll only distribute the blank solution files to svn
# to avoid conflicts
def copy_files(proj_dir):
    target_dir ="/home/ubuntu/Desktop/sol/"
    for i in range(4):
        shutil.copy(target_dir + "1.1.%d.c" % (i+1), os.path.join(proj_dir, "1.1.%d.c" % (i+1)))
    for i in range(11):
        shutil.copy(target_dir + "1.2.%d.c" % (i+1), os.path.join(proj_dir, "1.2.%d.c" % (i+1)))
    shutil.copy(target_dir + "1.1.1.S", os.path.join(proj_dir, "1.1.1.S"))
    shutil.copy(target_dir + "setcookie", os.path.join(proj_dir, "setcookie"))
    shutil.copy(target_dir + "Makefile", os.path.join(proj_dir, "Makefile"))
    shutil.copy(target_dir + "helper.c", os.path.join(proj_dir, "helper.c"))
    shutil.copy(target_dir + "shellcode.py", os.path.join(proj_dir, "shellcode.py"))

# create the cookie file from the student's netid
def set_cookie(uniqname):

    command = ["./setcookie",uniqname]
    subprocess.check_output(command)

def write_grade(filename, line):
    with open(filename,"a") as f:
        f.write(line)

def main():
    
    svn_root = "/home/ubuntu/Desktop/sp16-ece422/"
    curr_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    grade_file = svn_root+"../grade.txt"
    #grade_file = svn_root+"_class/_private/mp4/mp4_autograder/grade_"+curr_time+".txt"
    
    with open(svn_root+"_rosters/me.txt") as f:
    #with open(svn_root+"_rosters/students.txt") as f:
    #with open(svn_root+"_rosters/mp1_cp1_extension_list.txt") as f:
        for line in f:
            netid = line.strip()
            # commence grading
            grade = process(svn_root+netid+"/mp1",netid)
            if grade == -1:
                write_grade(grade_file,netid.strip()+","+"0,mp1 directory doesn't exist\n")
            with open(svn_root+netid+"/mp1/partners.txt") as p:
                partners_str = p.read().strip()
                if partners_str == '':
                    write_grade(grade_file,netid+", "+","+grade)
                else:
                    partners_list = partners_str.split('\n')
                    for nid in partners_list:
                        print nid
                        if nid == netid:
                            if(len(partners_list) == 1):
                                write_grade(grade_file,netid+", "+","+grade)
                            continue
                        else:
                            write_grade(grade_file,nid.strip()+","+netid+","+grade)
                            write_grade(grade_file,netid.strip()+","+nid+","+grade)


if __name__ == '__main__':
    main()
