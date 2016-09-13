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
time_sol = ['11031832']
attackerip_sol = ['10.46.1.105',
                  '10.46.1.106']
victimip_sol = ['10.46.1.103']

# look for solution file
time_filepath = "./5.1.5_time.txt"
attackerip_filepath = "./5.1.5_attackerip.txt"
victimip_filepath = "./5.1.5_victimip.txt"
if not (os.path.exists(time_filepath) and os.path.exists(attackerip_filepath) and os.path.exists(victimip_filepath)):
    print "0\tUnable to find your solution file(s).  Aborting."
else:

    # init return values
    score = 0;
    message = "\n";

    # start grading
    time_submission = read_solution(time_filepath)
    attackerip_submission = read_solution(attackerip_filepath)
    victimip_submission = read_solution(victimip_filepath)

    # grade first attack attempt time
    for ts in time_sol:
        if ts in time_submission:
            score += 1
            message += "file time passed\n"
        else:
            message += "file time failed\n"

    # grade attacker ip addresses
    score_aip = 0
    for aip in attackerip_submission:
        if aip in attackerip_sol:
            score_aip += 2
            message += (str(aip) + " passed\n")
        else:
            score_aip -= 1
            message += (str(aip) + " failed\n")

    if (len(attackerip_submission) < len(attackerip_sol)):
        message += ("attacker ip addresses insufficiently listed\n")

    if (score_aip < 0):
        score_aip = 0
    score += score_aip

    # grade victim ip address
    for vip in victimip_sol:
        if vip in victimip_submission:
            score += 3
            message += "victim ip passed\n"
        else:
            message += "victim ip failed\n"

    # print result
    print str(score)+"\t"+message;
    
