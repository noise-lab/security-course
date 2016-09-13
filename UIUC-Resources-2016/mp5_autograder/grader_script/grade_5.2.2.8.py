import os
import tools
from string import whitespace

def read_solution(filepath):
    data = ""
    with open(filepath,'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line[0] == "#":
                continue;
            data += line.lower()

    return data

# solution
sol = ['leet haxor']    # Leet Haxor
username_sol = ['root']

# look for solution file
metadata_filepath = "./5.2.2.8.txt"

if not (os.path.exists(metadata_filepath)):
    print "0\tUnable to find your solution file(s).  Aborting.\n"
else:
    # init return values
    score = 0
    message = "\n"

    # start grading
    metadata_submission = read_solution(metadata_filepath)

    # grade deleted filename
    if metadata_submission in sol:
        score += 5
        message += "metadata passed\n"
    elif metadata_submission in username_sol:
        score += 3
        message += "metadata partiall passed. username listed not full name\n"
    else:
        message += "metadata failed\n"

    # print result
    print str(score) + "\t" + message
