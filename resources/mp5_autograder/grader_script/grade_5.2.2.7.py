import os
import tools
from string import whitespace
import re
import check_plagiarism

def read_solution(filepath):
    data = []
    with open(filepath,'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line[0] == "#":
                continue;
            lines = re.split('[,\s]\s*',line)
            for line in lines:
                data.append(line)

    return data

def get_suspect_selection(filepath):
    with open(filepath, 'r') as f:
        line = f.read().strip()
        suspect = line[len(line)-1]
    return suspect

def get_location_selection(filepath):
    with open(filepath, 'r') as f:
        line = f.read().strip()
    return line

# solution
accomplice_l_sol = ['nefarious.accomplice.1995@gmail.com']
accomplice_w_sol = ['illini.pony.express@gmail.com']

accomplice_sol = {'1' : accomplice_l_sol,
                  '3' : accomplice_w_sol}

# original zoom
location_l_memorialstadium_sol = ['40.098', '-88.237']
location_l_isr_sol             = ['40.108', '-88.230']
location_l_eceb_sol            = ['40.114', '-88.228']
location_l_ncsa_sol            = ['40.114', '-88.223']
location_l_researchpark_sol    = ['40.092', '-88.238'] 

location_w_ikenberrycommons_sol = ['40.104', '-88.234']
location_w_bookstore_sol        = ['40.108', '-88.228']
location_w_morrowplots_sol      = ['40.104', '-88.226']
location_w_siebel_sol           = ['40.113', '-88.225']
location_w_washingtonpark_sol   = ['40.109', '-88.236']

location_sol = {'S6HmmW' : location_l_memorialstadium_sol,
                'DlGWvT' : location_l_isr_sol,
                'D0aaz1' : location_l_eceb_sol,
                '21dUSV' : location_l_ncsa_sol,
                '6q8OYH' : location_l_researchpark_sol,
                'dsHs4I' : location_w_ikenberrycommons_sol,
                'zvJvOE' : location_w_bookstore_sol,
                'WumlKB' : location_w_morrowplots_sol,
                'J7AkN4' : location_w_siebel_sol,
                'b4Hu4g' : location_w_washingtonpark_sol}

originaltime_sol = ['2200', '1000']

actualtime_l_sol = ['2140', '940']
actualtime_w_sol = ['unknown']

actualtime_sol = {'1' : actualtime_l_sol,
                  '3' : actualtime_w_sol}

# look for solution file
accomplice_filepath = "./5.2.2.7_accomplice.txt"
location_filepath = "./5.2.2.7_location.txt"
origtime_filepath = "./5.2.2.7_originaltime.txt"
acttime_filepath = "./5.2.2.7_actualtime.txt"

if not (os.path.exists(accomplice_filepath) and os.path.exists(location_filepath) and os.path.exists(origtime_filepath) and os.path.exists(acttime_filepath)):
    print "0\tUnable to find your solution file(s).  Aborting.\n"
else:
    # init return values
    score = 0
    message = "\n"

    # suspect/location selection
    suspect_path = "./suspect_vm.txt"
    location_path = "./code.txt"
    suspect = get_suspect_selection(suspect_path)
    location = get_location_selection(location_path)

    # start grading
    accomplice_submission = read_solution(accomplice_filepath)
    location_submission = read_solution(location_filepath)
    originaltime_submission = read_solution(origtime_filepath)
    actualtime_submission = read_solution(acttime_filepath)

    # grade accomplice contact email (5 points)
    for accs in accomplice_sol[suspect]:
        if accs in accomplice_submission:
            score += 5
            message += "accomplice passed\n"
        else:
            message += "accomplice failed\n"

    # grade location coordinates (+- 0.003 acceptance range) (6 points)
    for ci in range(0, len(location_submission)):
        min_coord = float(location_sol[location][ci]) - 0.002
        max_coord = float(location_sol[location][ci]) + 0.002
        if (float(location_submission[ci]) >= min_coord) and (float(location_submission[ci]) <= max_coord):
            score += 3
            if (ci == 0):
                message += "location(latitude) passed\n"
            elif (ci == 1):
                message += "location(longitude) passed\n"
        else:
            message += "location failed\n"

    # grade original escape time (4 points)
    for ots in originaltime_submission:
        ots = ots.replace(':', '')
        if ots in originaltime_sol:
            score += 4
            message += "original time passed\n"
            break
        else:
            message += "original time failed\n"
            break

    # grade actual escape time (5 points)
    for ats in actualtime_submission:
        ats = ats.lower()
        ats = ats.replace(':', '')
        if ats in actualtime_sol[suspect]:
            score += 5
            message += "actual time passed\n"
            break
        else:
            message += "actual time failed\n"
            break

    (copied, check_message) = check_plagiarism.check_plagiarism(location_submission)
    if copied == 1:
        score = 0
        message = check_message

    # print result
    print str(score) + "\t" + message
