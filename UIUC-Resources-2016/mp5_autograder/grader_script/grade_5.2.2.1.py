#!/usr/bin/python
import sys,os,subprocess,re;
from string import whitespace

def read_solution(filepath):
    data = []
    with open(filepath,'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line[0] == "#":
                continue;
            data.append(line)

    return data

def get_suspect_selection(filepath):
    with open(filepath, 'r') as f:
        line = f.read().strip()
        suspect = line[len(line)-1]
    return suspect

# solution
l_sol = ['l337h4x0r']
w_sol = ['wh1t3r0s3']

username_sol = {'1' : l_sol,
                '3' : w_sol}

# look for solution file
username_filepath = "./5.2.2.1.txt";

if not (os.path.exists(username_filepath)):
    print "0\tUnable to find your solution file(s).  Aborting.";
else:
    # init return values
    score = 0;
    message = "\n";

    # suspect selection
    suspect_path = "./suspect_vm.txt"
    suspect = get_suspect_selection(suspect_path)

    # start grading
    username_submission = read_solution(username_filepath)

    # grade suspect username
    if username_submission == username_sol[suspect]:
        score += 5
        message += ("username passed\n")

    else:
        message += ("Incorrect username submitted\n")

    # print result
    print str(score)+"\t"+message;
    
