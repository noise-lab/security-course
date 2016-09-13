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
            data.append(line.lower())

    return data

# solution
sol = ['cst', 'cdt']

# look for solution file
timezone_filepath = "./5.1.2.txt";
if not (os.path.exists(timezone_filepath)):
    print "0\tUnable to find your solution file(s).  Aborting.";
else:

    # init return values
    score = 0;
    message = "\n";

    # start grading
    timezone_submission = read_solution(timezone_filepath)

    for sub in timezone_submission:
        if sub in sol:
            score += 2
            message += ("timezone passed\n")

        else:
            message += ("timezone failed\n")

    # print result
    print str(score)+"\t"+message;
    
