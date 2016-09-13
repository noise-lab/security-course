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
                continue
            data.append(line)

    return data

def get_suspect_selection(filepath):
    with open(filepath, 'r') as f:
        line = f.read().strip()
        suspect = line[len(line)-1]
    return suspect

# solution
l_conversation_sol = ['alice.innocuous',
                      'alice.innocuous']
w_conversation_sol = ['ladiesman461',
                      'ladiesman461']

l_relationship_sol = ['e']
w_relationship_sol = ['b']

conversation_sol = {'1' : l_conversation_sol,
                    '3' : w_conversation_sol}

relationship_sol = {'1' : l_relationship_sol,
                    '3' : w_relationship_sol}

# look for solution file
conversation_filepath = "./5.2.2.2_usernames.txt"
relationship_filepath = "./5.2.2.2_relationship.txt"

if not (os.path.exists(conversation_filepath) and os.path.exists(relationship_filepath)):
    print "0\tUnable to find your solution file(s).  Aborting."
else:
    # init return values
    score = 0;
    message = "\n";

    # suspect selection
    suspect_path = "./suspect_vm.txt"
    suspect = get_suspect_selection(suspect_path)

    # start grading
    conversation_submission = read_solution(conversation_filepath)
    relationship_submission = read_solution(relationship_filepath)

    # grade conversation list
    suspect_sol = conversation_sol[suspect]
    for s in range(0, min(len(conversation_submission), len(suspect_sol))):
        if suspect_sol[s] in conversation_submission[s]:
            score += 1.25
            message += conversation_submission[s] + " passed\n"
        else:
            message += conversation_submission[s] + " failed\n"

    len_sub = len(conversation_submission)
    len_sol = len(suspect_sol)
    if len_sub > len_sol:
        for s in range (len_sol, len_sub):
            if conversation_submission[s] == 'ladiesman461':
                continue
            else:
                score -= 0.5
                break

    for rs in relationship_sol[suspect]:
        if rs in relationship_submission:
            score += 2.5
            message += "relationship passed\n"
            break
        else:
            message += "relationship failed\n"
            break
    
    # print result
    print str(score)+"\t"+message;
    
