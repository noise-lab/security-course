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

# solution
sol = ['ladiesman461']
display_name = ['Ladies Man']

# look for solution file
username_filepath = "./5.1.1.txt";
if not (os.path.exists(username_filepath)):
    print "0\tUnable to find your solution file(s).  Aborting.";
else:

    # init return values
    score = 0;
    message = "\n";

    # start grading
    username_submission = read_solution(username_filepath)

    for sub in username_submission:
        if sub in sol:
            score += 2
            message += ("username passed\n")

        else:
            message += ("username failed\n")

    # print result
    print str(score)+"\t"+message;
    
