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
FULL_CREDIT = 11
ROUNDS = 10
       
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
    for i in range(11):
        if error == 1:
            comment = "cannot compile"
            grade = 0
        else:
            grade = grade_app(proj_dir, i)
            comment = ""
            if isinstance(grade,int):
                if grade == 5:
                    comment ="Solution doesn't always work"
                elif grade == 9:
                    comment ="Did not redirect stderr"
                elif grade == 7:
                    comment ="Did not redirect stdout"
                elif grade == 6:
                    comment ="Did not redirect stderr nor stdout"
                elif grade == 0:
                    comment ="Solution does not work"
                elif grade == FULL_CREDIT:
                    if i <= 2:
                        grade = 8
                    elif i <= 6:
                        grade = 9
                    elif i <= 10:
                        grade = 10
            else:
                comment = grade
                grade = 0
        grades.append((grade, comment))

    global error
    error = 0

    try:
        kill_code = subprocess.check_call(["pkill", "-f", "/bin/sh"])
        kill_code = subprocess.check_call(["pkill", '-f', '/bin//sh'])
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
    tar = "1.2.%d" % (num+1)
    sol = "1.2.%d.py" % (num+1)

    if not os.path.exists(sol):
        return "no solution file"

    with open(sol) as f:
        f_content = f.read()
        if f_content == '':
            return "no submission"



    if num == 0 or num == 1:
        print os.path.basename(proj_dir), num
        stdout = subprocess.Popen(['python %s | ./%s' % (sol, tar)], stdout=subprocess.PIPE, shell=True).communicate()[0]
        print stdout
        # Grade respective for both parts
        if "Your grade is perfect" in stdout or 'A+' in stdout:
            return FULL_CREDIT
        else:
            return "Got %s." % (stdout)
    elif num <= 10:
        if num == 4:
            shellString = "python 1.2.5.py > tmp; ./1.2.5 tmp"
        else:
            shellString = './%s $(python %s)' %(tar, sol)

        print shellString
        
        if num == 9:
            run_shell_test(shellString)
            pt = 0
            if os.path.exists("stdin.txt"):
                pt = pt+6
                os.remove("stdin.txt")
            if os.path.exists("stdout.txt"):
                pt = pt+3
                os.remove("stdout.txt")
            if os.path.exists("stderr.txt"):
                pt = pt+1
                os.remove("stderr.txt")
            return pt
        elif num != 6:
            return run_shell_test(shellString)
        else:
            # This input is random... run it multiple times
            correct = 0
            wrong = 0
            for i in range(ROUNDS):
                if run_shell_test(shellString, .2) == FULL_CREDIT:
                    correct += 1
                else:
                    wrong += 1

            if correct == ROUNDS:
                return FULL_CREDIT
            if wrong == ROUNDS:
                return 'Shell was not running'
            else:
                return 5
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
    #with open(svn_root+"_rosters/mp4_cp2_extension_list.txt") as f:
    #with open(svn_root+"_rosters/students.txt") as f:
        for line in f:
            netid = line.strip()
            # commence grading
            grade = process(svn_root+netid+"/mp1",netid)
            if grade == -1:
                write_grade(grade_file,netid.strip()+","+"0,mp1 directory doesn't exit\n")
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
