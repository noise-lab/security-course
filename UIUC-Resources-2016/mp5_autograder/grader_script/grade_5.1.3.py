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
sol = ['wh1t3r0s3',
       'alice.innocuous',
       'alice.innocuous',
       'wh1t3r0s3']

# look for solution file
conversation_filepath = "./5.1.3.txt";
if not (os.path.exists(conversation_filepath)):
    print "0\tUnable to find your solution file(s).  Aborting.";
else:

    # init return values
    score = 0;
    message = "\n";

    # start grading
    conversation_submission = read_solution(conversation_filepath)

    # domain name included
    domain = '@jwchat.org'
    penalty = 0
    for s in range(0, len(conversation_submission)):
        index = conversation_submission[s].find('@')
        domain_sub = conversation_submission[s][index:]
        if index != -1 and domain_sub == domain:
            if penalty == 0:
                score -= 1
                penalty = 1
            conversation_submission[s] = conversation_submission[s][:index].rstrip()

    for s in range(0, len(conversation_submission)):
        # case where the last chat history is recorded: wh1t3r0s3 left message but not a conversation
        if s >= len(sol):
            if conversation_submission[s] == sol[len(sol)-1]:
                message += conversation_submission[s] + " not considered a conversation but ok\n"
            continue
        else:
            if sol[s] == conversation_submission[s]:
                score += 1
                message += sol[s] + " passed\n"
            else:
                message += sol[s] + " failed\n"
    
    # assign point if last username is matched: listed alice.innocuous only once in the middle
    if len(conversation_submission) == len(sol) - 1:
        if conversation_submission[len(conversation_submission)-1] == sol[len(sol)-1]:
            score += 1
            message += sol[len(sol)-1] + " passed\n"

    # minimum score = 0
    if score <= 0.0:
        score = 0

    # print result
    print str(score)+"\t"+message;
    
