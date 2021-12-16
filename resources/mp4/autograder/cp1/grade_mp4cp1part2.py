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


def q1(svndir, sol, max_score):
    message = ""
    score = 0
    filepath = "{}/4.1.2.1.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and (sol in submitted):
            score += max_score
            message += "\t+{} year: pass\n".format(max_score)
        else:
            message += "\t+{} year: fail\n".format(0)

    header = "4.1.2.1\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q2(svndir, sol, max_score):
    sol = sol.lower()
    message = ""
    score = 0
    filepath = "{}/4.1.2.2.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and (sol in submitted):
            score += max_score
            message += "\t+{} hostname: pass\n".format(max_score)
        else:
            message += "\t+{} hostname: fail\n".format(0)

    header = "4.1.2.2\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q3(svndir, sol, max_score):
    sol1 = sol[0]
    sol2 = sol[1]
    sol1 = map(lambda x: x.lower(), sol1)
    sol2 = map(lambda x: x.lower(), sol2)
    sol1.sort()
    sol2.sort()
    message = ""
    score = 0
    filepath = "{}/4.1.2.3.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        submitted.sort()
        if (len(submitted) == len(sol1)) and ((submitted == sol1) or (submitted == sol2)):
            score += max_score
            message += "\t+{} cipher suite list: pass\n".format(max_score)
        else:
            #passed = 0
            #if len(submitted) == len(sol):
            #    for i in range(len(submitted)):
            #        if submitted[i] in sol[i]:
            #            passed += 1
            #if passed == len(sol):
            #    score += max_score
            #    message += "\t+{} cipher suite list: pass\n".format(max_score)
            #else:
            message += "\t+{} cipher suite list: fail\n".format(0)

    header = "4.1.2.3\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q4(svndir, sol, max_score):
    sol = sol.lower()
    message = ""
    score = 0
    filepath = "{}/4.1.2.4.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and (sol in submitted):
            score += max_score
            message += "\t+{} chosen cipher suite: pass\n".format(max_score)
        else:
            message += "\t+{} chosen cipher suite: fail\n".format(0)

    header = "4.1.2.4\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q5(svndir, sol, max_score):
    sol = sol.lower()
    message = ""
    score = 0
    filepath = "{}/4.1.2.5.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and (sol in submitted[0]):
            score += max_score
            message += "\t+{} first name: pass\n".format(max_score)
        else:
            message += "\t+{} first name: fail\n".format(0)

    header = "4.1.2.5\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q6(svndir, sol, max_score):
    sol = sol.strip().lower().replace("'","").strip("~")
    message = ""
    score = 0
    filepath = "{}/4.1.2.6.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if len(submitted) == 1:
            submitted = submitted[0].replace("'","").replace(" ","%20")
            if sol in submitted:
                score += max_score
                message += "\t+{} message sent: pass\n".format(max_score)
            else:
                message += "\t+{} message sent: fail\n".format(0)
        else:
            message += "\t+{} message sent: fail\n".format(0)

    header = "4.1.2.6\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q7(svndir, sol, max_score):
    sol = sol.lower()
    message = ""
    score = 0
    filepath = "{}/4.1.2.7.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and (sol in submitted[0]):
            score += max_score
            message += "\t+{} cookie: pass\n".format(max_score)
        else:
            message += "\t+{} cookie: fail\n".format(0)

    header = "4.1.2.7\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def grade_mp4cp1part2(svndir, student, solution_path):
    json_data = open(solution_path).read()
    sol = json.loads(json_data)
    common_sol = sol["common"]
    unique_sol = sol[student]

    message = ""
    score = 0
    total = 0
    (message, score, total) = tuple(map(operator.add, (message, score, total), q1(svndir, common_sol["year"], 1)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q2(svndir, common_sol["hostname"], 1)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q3(svndir, common_sol["ciphersuite-list"], 1)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q4(svndir, common_sol["server-ciphersuite"], 1)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q5(svndir, common_sol["name"], 2)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q6(svndir, unique_sol["msg"], 3)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q7(svndir, common_sol["cookie"], 1)))
    header = "4.1.2\t {} / {}\n".format(score, total)

    return header + message, score, total
