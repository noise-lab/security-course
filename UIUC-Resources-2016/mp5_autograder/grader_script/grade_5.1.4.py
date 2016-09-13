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
            # data+=line

    return data

# solution
name_sol = ['suicidenote.doc']
time_sol = ['11041937']

# look for solution file
name_filepath = "./5.1.4_name.txt"
time_filepath = "./5.1.4_time.txt"
if not (os.path.exists(name_filepath) and os.path.exists(time_filepath)):
    print "0\tUnable to find your solution file(s).  Aborting."
else:

    # init return values
    score = 0;
    message = "\n";

    # start grading
    name_submission = read_solution(name_filepath)
    time_submission = read_solution(time_filepath)

    # grade file name
    for ns in name_submission:
        if ns in name_sol:
            score += 2
            message += "file name passed\n"
        else:
            message += "file name failed\n"

    # grade file modified time
    for ts in time_submission:
        if ts in time_sol:
            score += 2
            message += "file time passed\n"
        else:
            message += "file time failed\n"

    # print result
    print str(score)+"\t"+message;
    
