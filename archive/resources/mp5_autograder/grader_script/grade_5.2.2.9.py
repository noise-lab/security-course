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

def get_suspect_selection(filepath):
    with open(filepath, 'r') as f:
        line = f.read().strip()
        suspect = line[len(line)-1]
    return suspect

# solution
l_sol = ['yes']
w_sol = ['no']

sol = {'1' : l_sol,
       '3' : w_sol}

# look for solution file
decision_filepath = "./5.2.2.9.txt"

if not (os.path.exists(decision_filepath)):
    print "0\tUnable to find your solution file(s).  Aborting.\n"
else:
    # init return values
    score = 0
    message = "\n"

    # suspect selection
    suspect_path = "./suspect_vm.txt"
    suspect = get_suspect_selection(suspect_path)

    # start grading
    decision_submission = read_solution(decision_filepath)

    # grade deleted filename
    for ds in sol[suspect]:
        if ds in decision_submission:
            score += 5
            message += "decision passed\n"
        else:
            message += "decision failed\n"
        
    # print result
    print str(score) + "\t" + message
