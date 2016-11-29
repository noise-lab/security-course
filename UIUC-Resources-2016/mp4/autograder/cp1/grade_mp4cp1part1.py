#!/usr/bin/python
import json
import os
import operator


def read_lines(filepath):
    content = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.split('#')[0]
            line = line.strip()
            if (len(line) == 0) or (line[0] == '#'):
                continue
            content.append(line.lower())
    return list(set(content))


def q1(svndir, solutions, max_score):
    a_sol = map(lambda x: x.lower(), solutions["ip"])
    a_sol.sort()
    b_sol = map(lambda x: x.lower(), solutions["mac"])
    b_sol.sort()
    message = ""
    score = 0
    a_filepath = "{}/4.1.1.1_ip.txt".format(svndir)
    b_filepath = "{}/4.1.1.1_mac.txt".format(svndir)
    if not (os.path.exists(a_filepath) and os.path.exists(b_filepath)):
        message += "\t+{} unable to find your solution file(s)...\n".format(0)
    else:
        # start grading
        a_submitted = read_lines(a_filepath)
        a_submitted.sort()
        b_submitted = read_lines(b_filepath)
        b_submitted.sort()
        if (len(a_submitted) != 0) and (len(b_submitted) != 0):
            if ((set(a_sol) <= set(a_submitted)) and (set(b_sol) <= set(b_submitted))) or ((set(a_submitted) <= set(a_sol+["8.8.4.4","224.0.0.251"])) and (set(b_submitted) <= set(b_sol + ["01:00:5e:00:00:fb"]))):
                score += 1
                message += "\t+{} valid ip and mac address: pass\n".format(1)
            else:
                message += "\t+{} valid ip and mac address: fail\n".format(0)
        else:
            message += "\t+{} valid ip and mac address: fail\n".format(0)
        if a_submitted == a_sol:
            score += 1
            message += "\t+{} local ip address: pass\n".format(1)
        else:
            message += "\t+{} local ip address: fail\n".format(0)

        if b_submitted == b_sol:
            score += 1
            message += "\t+{} local mac address: pass\n".format(1)
        else:
            message += "\t+{} local mac address: fail\n".format(0)

    header = "4.1.1.1\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q2(svndir, sol, max_score):
    message = ""
    score = 0
    filepath = "{}/4.1.1.2.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and (sol in submitted):
            score += max_score
            message += "\t+{} number of tcp conversation: pass\n".format(max_score)
        else:
            message += "\t+{} number of tcp conversation: fail\n".format(0)

    header = "4.1.1.2\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q3(svndir, sol, max_score):
    message = ""
    score = 0
    filepath = "{}/4.1.1.3.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and (sol in submitted):
            score += max_score
            message += "\t+{} gateway ip: pass\n".format(max_score)
        else:
            message += "\t+{} gateway ip: fail\n".format(0)

    header = "4.1.1.3\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q4(svndir, solutions, max_score):
    a_sol = solutions["active"].strip().lower().replace("'", "")
    b_sol = solutions["passive"].strip().lower().replace("'", "")
    message = ""
    score = 0
    a_filepath = "{}/4.1.1.4_active.txt".format(svndir)
    b_filepath = "{}/4.1.1.4_passive.txt".format(svndir)
    if not (os.path.exists(a_filepath) and os.path.exists(b_filepath)):
        message += "\t+{} unable to find your solution file(s)...\n".format(0)
    else:
        # start grading
        a_submitted = read_lines(a_filepath)
        if len(a_submitted) == 0:
            a_submitted += [""]
        if len(a_submitted) == 1:
            a_submitted = a_submitted[0].split('\\')[0].replace("'", "").strip()
            a_submitted = "".join([i if ord(i) < 128 else "" for i in a_submitted])
            if a_submitted == a_sol:
                score += 1
                message += "\t+{} identifying active ftp: pass\n".format(1)
            else:
                message += "\t+{} identifying active ftp: fail\n".format(0)
        else:
            message += "\t+{} identifying active ftp: fail\n".format(0)

        b_submitted = read_lines(b_filepath)
        if len(b_submitted) == 0:
            b_submitted += [""]
        if len(b_submitted) == 1:
            b_submitted = b_submitted[0].split('\\')[0].replace("'", "").strip()
            b_submitted = "".join([i if ord(i) < 128 else "" for i in b_submitted])
            if b_submitted == b_sol:
                score += 1
                message += "\t+{} identifying passive ftp: pass\n".format(1)
            else:
                message += "\t+{} identifying passive ftp: fail\n".format(0)
        else:
            message += "\t+{} identifying passive ftp: fail\n".format(0)
        sol_list = [a_sol, b_sol]
        if (a_submitted in sol_list) and (b_submitted in sol_list):
            score += 1
            message += "\t+{} content retrieval: pass\n".format(1)
        else:
            message += "\t+{} content retrieval: fail\n".format(0)

    header = "4.1.1.4\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q5(svndir, sol, max_score):
    message = ""
    score = 0
    filepath = "{}/4.1.1.5.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and (sol in submitted):
            score += max_score
            message += "\t+{} port scanner ip: pass\n".format(max_score)
        else:
            message += "\t+{} port scanner ip: fail\n".format(0)

    header = "4.1.1.5\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def grade_mp4cp1part1(svndir, student, solution_path):
    json_data = open(solution_path).read()
    sol = json.loads(json_data)
    common_sol = sol["common"]
    unique_sol = sol[student]

    message = ""
    score = 0
    total = 0
    (message, score, total) = tuple(map(operator.add, (message, score, total), q1(svndir, unique_sol, 3)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q2(svndir, common_sol["tcp"], 1)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q3(svndir, unique_sol["gw"], 2)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q4(svndir, unique_sol, 3)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q5(svndir, unique_sol["portscan"], 1)))
    header = "4.1.1\t {} / {}\n".format(score, total)

    return header + message, score, total
