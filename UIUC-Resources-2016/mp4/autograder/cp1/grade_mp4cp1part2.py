#!/usr/bin/python
import json
import os
import operator


def read_lines(filepath):
    content = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if (len(line) == 0) or (line[0] == '#'):
                continue
            content.append(line.lower())
    return content


def q1(svndir, solutions, max_score):
    sol = solutions["year"]
    message = ""
    score = 0
    filepath = "{}/4.1.2.1.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and (submitted[0] == sol):
            score += 1
            message += "\t+{} year: pass\n".format(1)
        else:
            message += "\t+{} year: fail\n".format(0)

    header = "4.1.2.1\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q2(svndir, solutions, max_score):
    sol = solutions["hostname"].lower()
    message = ""
    score = 0
    filepath = "{}/4.1.2.2.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and (submitted[0] == sol):
            score += 1
            message += "\t+{} hostname: pass\n".format(1)
        else:
            message += "\t+{} hostname: fail\n".format(0)

    header = "4.1.2.2\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q3(svndir, solutions, max_score):
    sol = map(lambda x: x.lower(), solutions["ciphersuite-list"])
    sol.sort()
    message = ""
    score = 0
    filepath = "{}/4.1.2.3.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        submitted.sort()
        if (len(submitted) == len(sol)) and (submitted == sol):
            score += 1
            message += "\t+{} cipher suite list: pass\n".format(1)
        else:
            passed = 0
            if len(submitted) == len(sol):
                for i in range(len(submitted)):
                    if submitted[i] in sol[i]:
                        passed += 1
            if passed == len(sol):
                score += 1
                message += "\t+{} cipher suite list: pass\n".format(1)
            else:
                message += "\t+{} cipher suite list: fail\n".format(0)

    header = "4.1.2.3\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q4(svndir, solutions, max_score):
    sol = solutions["server-ciphersuite"].lower()
    message = ""
    score = 0
    filepath = "{}/4.1.2.4.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and ((submitted[0] == sol) or (submitted[0] in sol)):
            score += 1
            message += "\t+{} chosen cipher suite: pass\n".format(1)
        else:
            message += "\t+{} chosen cipher suite: fail\n".format(0)

    header = "4.1.2.4\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q5(svndir, solutions, max_score):
    sol = solutions["name"].lower()
    message = ""
    score = 0
    filepath = "{}/4.1.2.5.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and (submitted[0] == sol):
            score += 2
            message += "\t+{} first name: pass\n".format(2)
        else:
            message += "\t+{} first name: fail\n".format(0)

    header = "4.1.2.5\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q6(svndir, solutions, max_score):
    sol = solutions["msg"].lower()
    alt_sol = \
        "\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c " \
        "\u043d\u044e\u0445\u0430\u044e\u0442 my wifi!"
    message = ""
    score = 0
    filepath = "{}/4.1.2.6.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and ((submitted[0] == sol) or (submitted[0] == alt_sol)):
            score += 3
            message += "\t+{} message sent: pass\n".format(3)
        else:
            message += "\t+{} message sent: fail\n".format(0)

    header = "4.1.2.6\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q7(svndir, solutions, max_score):
    sol = solutions["cookie"].lower()
    message = ""
    score = 0
    filepath = "{}/4.1.2.7.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and (submitted[0] == sol):
            score += 1
            message += "\t+{} cookie: pass\n".format(1)
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
    (message, score, total) = tuple(map(operator.add, (message, score, total), q1(svndir, common_sol, 1)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q2(svndir, common_sol, 1)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q3(svndir, common_sol, 1)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q4(svndir, common_sol, 1)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q5(svndir, common_sol, 2)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q6(svndir, unique_sol, 3)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q7(svndir, common_sol, 1)))
    header = "4.1.2\t {} / {}\n".format(score, total)

    return header + message, score, total
