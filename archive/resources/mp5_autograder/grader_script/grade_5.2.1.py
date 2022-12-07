import os
import tools
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

def read_solution_string(filepath):
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
default_sol = ['puppy', '431']       # Puppy Linux 4.3.1
behavior_script_sol = ['pupsave.2fs', '40_custom', 'dd', 'rc.sysinit']
primary_l_sol = ['ubuntu', '1510']   # Linux Ubuntu 15.10
primary_w_sol = ['ubuntu', '1404']   # Linux Ubuntu 14.04

primary_sol = {'1' : primary_l_sol,
               '3' : primary_w_sol}

# primary_sol = {'l' : primary_l_sol,
#                'w' : primary_w_sol}

# look for solution file
default_filepath = "./5.2.1_default.txt"
behavior_filepath = "./5.2.1_behavior.txt"
primary_filepath = "./5.2.1_primary.txt"

if not (os.path.exists(default_filepath) and os.path.exists(behavior_filepath) and os.path.exists(primary_filepath)):
    print "0\tUnable to find your solution file(s).  Aborting.\n"
else:
    # init return values
    score = 0
    message = "\n"

    # suspect selection
    suspect_path = "./suspect_vm.txt"
    suspect = get_suspect_selection(suspect_path)

    # start grading
    default_submission = read_solution(default_filepath)
    behavior_submission = read_solution_string(behavior_filepath)
    primary_submission = read_solution(primary_filepath)

    # grade default os
    for ds in range(0, len(default_submission)):
        d_sub = default_submission[ds].replace(".", "")
        if default_sol[ds] in d_sub:
            score += 1.25
            message += default_submission[ds] + " passed\n"
        else:
            message += default_submission[ds] + " failed\n"
    if score >= 2.5:
        score = 2.5

    # grade default os behavior (TODO)
    if behavior_submission in behavior_script_sol[0]:
        score += 5
        message += behavior_submission + " passed\n"
    elif behavior_submission in behavior_script_sol[1] or behavior_submission in behavior_script_sol[2]:
        score += 3
        message += behavior_submission + " acceptable but not the main script\n"
    elif behavior_submission in behavior_script_sol[3]:
        score += 2
        message += behavior_submission + " acceptable but this script does not exist in file system\n"
    else:
        message += "script failed\n"

    # grade primary os
    for ps in range(0, len(primary_submission)):
        p_sub = primary_submission[ps].replace(".", "")
        if primary_sol[suspect][ps] in p_sub:
            score += 1.25
            message += primary_submission[ps] + " passed\n"
        else:
            message += primary_submission[ps] + " failed\n"
            
    # print result
    print str(score) + "\t" + message
