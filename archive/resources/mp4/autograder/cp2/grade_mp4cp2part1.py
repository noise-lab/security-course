#!/usr/bin/python
import json
import os
import operator
import hmac
import subprocess
import hashlib
import base64
import filecmp


def read_lines(filepath, case_sensitive=False, no_comment=False):
    content = []
    with open(filepath, 'r') as f:
        for line in f:
            if not no_comment:
                line = line.split('#')[0]
            line = line.strip()
            if (len(line) == 0) or (line[0] == '#'):
                continue
            if not case_sensitive:
                line = line.lower()
            content.append(line)
    return content


def q1(svndir, sol, max_score):
    message = ""
    zero = float(0)
    score = zero
    filepath = "{}/4.2.1.1.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(zero)
    else:
        # start grading
        case_sensitive = True
        submitted = list(set(read_lines(filepath, case_sensitive)))
        if (len(submitted) == 1) and (submitted[0] == sol):
            score += max_score
            message += "\t+{} wep key: pass\n".format(max_score)
        else:
            message += "\t+{} wep key: fail\n".format(zero)

    header = "4.2.1.1\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q2(svndir, sol, max_score):
    client1 = sol["client1"]
    client2 = sol["client2"]
    server = sol["server"]
    part_score = max_score/2
    message = ""
    zero = float(0)
    score = zero
    filepath = "{}/4.2.1.2.txt".format(svndir)
    if not (os.path.exists(filepath)):
        message += "\t+{} unable to find your solution file(s)...\n".format(zero)
    else:
        # start grading
        submitted = list(set(read_lines(filepath)))
        submitted.sort()
        # check if server included
        if server in submitted:
            server_filepath = "{}/4.2.1.3.txt".format(svndir)
            if os.path.exists(server_filepath):
                server_submitted = list(set(read_lines(server_filepath)))
                if (len(server_submitted) == 1) and (server == server_submitted[0]):
                    submitted.remove(server)
        if (client1 in submitted) or (client2 in submitted):
            score += max_score
            message += "\t+{} client ip: pass\n".format(max_score)
            if client1 in submitted:
                submitted.remove(client1)
            if client2 in submitted:
                submitted.remove(client2)
        else:
            message += "\t+{} client ip: fail\n".format(zero)
#        if client2 in submitted:
#            score += part_score
#            message += "\t+{} client2 ip: pass\n".format(part_score)
#            while client2 in submitted:
#                submitted.remove(client2)
#        else:
#            message += "\t+{} client2 ip: fail\n".format(0)

        # check false positives (-1 each)
        false_positive = len(submitted)
        if false_positive > 0:
            score -= false_positive
            score = zero if score < 0 else score
            message += "\t-{} false positives found: {}\n".format(float(false_positive), false_positive)

    header = "4.2.1.2\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q3(svndir, sol, max_score):
    server = sol["server"]
    message = ""
    zero = float(0)
    score = zero
    filepath = "{}/4.2.1.3.txt".format(svndir)
    if not (os.path.exists(filepath)):
        message += "\t+{} unable to find your solution file(s)...\n".format(zero)
    else:
        # start grading
        submitted = list(set(read_lines(filepath)))
        submitted.sort()
        total_submitted = len(submitted)
        if server in submitted:
            score += max_score
            message += "\t+{} server ip: pass\n".format(max_score)
            while server in submitted:
                submitted.remove(server)
        else:
            message += "\t+{} server ip: fail\n".format(zero)

        # check false positives (-1 each)
        false_positive = len(submitted)
        if false_positive > 0:
            penalty = max_score*false_positive/total_submitted
            score -= penalty
            score = zero if score < 0 else score
            message += "\t-{} false positives found: {}\n".format(float(penalty), false_positive)

    header = "4.2.1.3\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q4(svndir, solutions, max_score):
    message = ""
    part_score = max_score/len(solutions)
    zero = float(0)
    score = zero
    filepath = "{}/4.2.1.4.txt".format(svndir)
    if not (os.path.exists(filepath)):
        message += "\t+{} unable to find your solution file(s)...\n".format(zero)
    else:
        # start grading
        submitted = list(set(read_lines(filepath)))

        # ignore ftp-data
        if "ftp-data" in submitted:
            submitted.remove("ftp-data")

        # check ftp
        sol = solutions["ftp"]
        if sol in submitted:
            score += part_score
            message += "\t+{} ftp: pass\n".format(part_score)
            while sol in submitted:
                submitted.remove(sol)
        else:
            message += "\t+{} ftp: fail\n".format(zero)

        # check http
        sol = solutions["http"]
        if sol in submitted:
            score += part_score
            message += "\t+{} http: pass\n".format(part_score)
            while sol in submitted:
                submitted.remove(sol)
        else:
            message += "\t+{} http: fail\n".format(zero)

        # check https
        sol = solutions["https"]
        if (sol[0] in submitted) or (sol[1] in submitted) or (sol[2] in submitted) or (sol[3] in submitted):
            score += part_score
            message += "\t+{} https: pass\n".format(part_score)
            while (sol[0] in submitted) or (sol[1] in submitted) or (sol[2] in submitted) or (sol[3] in submitted):
                if sol[0] in submitted:
                    submitted.remove(sol[0])
                if sol[1] in submitted:
                    submitted.remove(sol[1])
                if sol[2] in submitted:
                    submitted.remove(sol[2])
                if sol[3] in submitted:
                    submitted.remove(sol[3])
        else:
            message += "\t+{} https: fail\n".format(zero)

        # check dhcp
        sol = solutions["dhcp"]
        if (sol[0] in submitted) or (sol[1] in submitted):
            score += part_score
            message += "\t+{} dhcp: pass\n".format(part_score)
            while (sol[0] in submitted) or (sol[1] in submitted):
                if sol[0] in submitted:
                    submitted.remove(sol[0])
                if sol[1] in submitted:
                    submitted.remove(sol[1])
        else:
            message += "\t+{} dhcp: fail\n".format(zero)

        # check false positives (-1 each)
        false_positive = len(submitted)
        if false_positive > 0:
            score -= false_positive
            score = zero if score < 0 else score
            message += "\t-{} false positives found: {}\n".format(float(false_positive), false_positive)

    header = "4.2.1.4\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q5(svndir, solutionpath, max_score):
    message = ""
    zero = float(0)
    score = zero
    filepath = "{}/4.2.1.5.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(zero)
    else:
        # start grading
        if filecmp.cmp(filepath, solutionpath):
            score += max_score
            message += "\t+{} server secret: pass\n".format(max_score)
        else:
            message += "\t+{} server secret: fail\n".format(zero)

    header = "4.2.1.5\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


# validate credentials
def check_cred(username, password):
    h = hmac.new(key_password, username, hashlib.sha256)
    digest = h.hexdigest()
    expected = digest[0:12]
    # get the information out of the password (the other characters are timestamp)
    actual = password[0:2] + password[3] + password[5:7] + password[9] + password[11:13] + \
             password[14] + password[16] + password[18:20]
    return expected == actual


def q6(svndir, max_score):
    # init return values
    zero = float(0)
    score = zero
    message = ""
    filepath = "{}/4.2.1.6.txt".format(svndir)
    username = None

    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(zero)
    else:
        submitted = read_lines(filepath)
        num_line = len(submitted)
        if num_line == 2:
            username = submitted[0]
            password = submitted[1]
            if len(password) != 20:
                message += "\t+{} login credentials: fail - password length should be 20\n".format(zero)
            elif check_cred(username, password):
                score += max_score
                message += "\t+{} login credentials: pass\n".format(max_score)
            else:
                message += "\t+{} login credentials: fail - mismatch\n".format(zero)
        else:
            message += "\t+{} login credentials: fail - 1 username and 1 password expected\n".format(zero)

    header = "4.2.1.6\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score, username


# validate secret message
def check_secret(username, submitted, student, max_score):
    zero = float(0)
    score = zero
    part_score = float(max_score)/2
    message = ""
    num_line = len(submitted)
    if num_line > 0:
        if num_line > 1:
            submitted = ''.join(submitted)
        elif num_line == 1:
            submitted = submitted[0]
        if submitted in message_list:
            message_list[submitted].append(student)
        else:
            message_list[submitted] = [student]
        pipe = subprocess.Popen(['openssl', 'aes256', '-d', '-nosalt', '-k', key_message],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output = pipe.communicate(base64.b64decode(submitted))
            data = json.loads(output[0])
            # print(data['user']['name'])
            # print(data)
            score += part_score
            message += "\t+{} secret message: pass\n".format(part_score)
            if username is None or (data['user']['name'] != username):
                message += "\t+{} username match: fail - {} != {}\n".format(zero, data['user']['name'], username)
            else:
                score += part_score
                message += "\t+{} username match: pass\n".format(part_score)
        except (ValueError, TypeError):
            message += "\t+{} secret message: fail - unable to decrypt\n".format(zero)
    else:
        message += "\t+{} secret message: fail - no secret message found\n".format(zero)
    return score, message


def q7(svndir, username, student, max_score):
    # init return values
    zero = float(0)
    score = zero
    message = ""
    filepath = "{}/4.2.1.7.txt".format(svndir)

    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(zero)
    else:
        case_sensitive = True
        no_comment = True
        submitted = list(set(read_lines(filepath, case_sensitive, no_comment)))
        (score, message) = tuple(map(operator.add, (score, message),
                                     check_secret(username, submitted, student, max_score)))

    header = "4.2.1.7\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q8(svndir, sol, max_score):
    message = ""
    zero = float(0)
    score = zero
    filepath = "{}/4.2.1.8.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(zero)
    else:
        # start grading
        submitted = list(set(read_lines(filepath)))
        if (len(submitted) == 1) and (submitted[0] == sol):
            score += max_score
            message += "\t+{} number of years in jail: pass\n".format(max_score)
        else:
            message += "\t+{} number of years in jail: fail\n".format(zero)

    header = "4.2.1.8\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


message_list = dict()
key_message = "show me the money operation cwal"
key_password = "power overwhelming black sheep wall"


def grade_mp4cp2part1(svndir, solution_path, student):
    json_data = open(solution_path + "/cp2_sol.json").read()
    sol = json.loads(json_data)

    message = ""
    zero = float(0)
    score = zero
    total = zero
    (message, score, total) = tuple(map(operator.add, (message, score, total), q1(svndir, sol["wep"], float(15))))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q2(svndir, sol["ip"], float(5))))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q3(svndir, sol["ip"], float(5))))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q4(svndir, sol["protocol"], float(12))))
    server_key = solution_path + "/server.key"
    (message, score, total) = tuple(map(operator.add, (message, score, total), q5(svndir, server_key, float(5))))
    q6_message, q6_score, q6_total, username = q6(svndir, float(20))
    (message, score, total) = tuple(map(operator.add, (message, score, total), (q6_message, q6_score, q6_total)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q7(svndir, username, student, float(6))))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q8(svndir, sol["year"], float(2))))
    header = "4.2.1\t {} / {}\n".format(score, total)

    return header + message, score, total, message_list
