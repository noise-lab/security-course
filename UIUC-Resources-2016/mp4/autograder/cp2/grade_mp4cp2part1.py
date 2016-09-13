#!/usr/bin/python
import json
import os
import operator
import hmac
import subprocess
import hashlib
import base64


def read_lines(filepath, case_sensitive=False):
    content = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if (len(line) == 0) or (line[0] == '#'):
                continue
            if not case_sensitive:
                line = line.lower()
            content.append(line)
    return content


def q1(svndir, solutions, max_score):
    sol = solutions["wep"]
    message = ""
    score = 0
    filepath = "{}/4.2.1.1.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        case_sensitive = True
        submitted = read_lines(filepath, case_sensitive)
        if (len(submitted) == 1) and (submitted[0] == sol):
            score += 10
            message += "\t+{} wep key: pass\n".format(10)
        else:
            message += "\t+{} wep key: fail\n".format(0)

    header = "4.2.1.1\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q2(svndir, solutions, max_score):
    sol = solutions["ip"]
    server = sol["server"]
    client1 = sol["client1"]
    client2 = sol["client2"]
    message = ""
    score = 0
    filepath = "{}/4.2.1.2.txt".format(svndir)
    if not (os.path.exists(filepath)):
        message += "\t+{} unable to find your solution file(s)...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        submitted.sort()
        if server in submitted:
            score += 2
            message += "\t+{} server ip: pass\n".format(2)
            while server in submitted:
                submitted.remove(server)
        else:
            message += "\t+{} server ip: fail\n".format(0)
        if client1 in submitted:
            score += 2
            message += "\t+{} client1 ip: pass\n".format(2)
            while client1 in submitted:
                submitted.remove(client1)
        else:
            message += "\t+{} client1 ip: fail\n".format(0)
        if client2 in submitted:
            score += 2
            message += "\t+{} client2 ip: pass\n".format(2)
            while client2 in submitted:
                submitted.remove(client2)
        else:
            message += "\t+{} client2 ip: fail\n".format(0)

        # check false positives (-1 each)
        false_positive = len(submitted)
        if false_positive > 0:
            score -= false_positive
            score = 0 if score < 0 else score
            message += "\t-{} false positives found: {}\n".format(false_positive, false_positive)

    header = "4.2.1.2\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q3(svndir, solutions, max_score):
    message = ""
    score = 0
    filepath = "{}/4.2.1.3.txt".format(svndir)
    if not (os.path.exists(filepath)):
        message += "\t+{} unable to find your solution file(s)...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)

        # ignore ftp-data
        while "ftp-data" in submitted:
            submitted.remove("ftp-data")

        # check ftp (3 points)
        sol = solutions["ftp"]
        if sol in submitted:
            score += 3
            message += "\t+{} ftp: pass\n".format(3)
            while sol in submitted:
                submitted.remove(sol)
        else:
            message += "\t+{} ftp: fail\n".format(0)

        # check https (3 points)
        sol = solutions["https"]
        if (sol[0] in submitted) or (sol[1] in submitted) or (sol[2] in submitted) or (sol[3] in submitted):
            score += 3
            message += "\t+{} https: pass\n".format(3)
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
            message += "\t+{} https: fail\n".format(0)

        # check http (3 points)
        sol = solutions["http"]
        if (sol[0] in submitted) or (sol[1] in submitted):
            score += 3
            message += "\t+{} http: pass\n".format(3)
            while (sol[0] in submitted) or (sol[1] in submitted):
                if sol[0] in submitted:
                    submitted.remove(sol[0])
                if sol[1] in submitted:
                    submitted.remove(sol[1])
        else:
            message += "\t+{} http: fail\n".format(0)

        # check dhcp (3 points)
        sol = solutions["dhcp"]
        if (sol[0] in submitted) or (sol[1] in submitted):
            score += 3
            message += "\t+{} dhcp: pass\n".format(3)
            while (sol[0] in submitted) or (sol[1] in submitted):
                if sol[0] in submitted:
                    submitted.remove(sol[0])
                if sol[1] in submitted:
                    submitted.remove(sol[1])
        else:
            message += "\t+{} dhcp: fail\n".format(0)

        # check false positives (-1 each)
        false_positive = len(submitted)
        if false_positive > 0:
            score -= false_positive
            score = 0 if score < 0 else score
            message += "\t-{} false positives found: {}\n".format(false_positive, false_positive)

    header = "4.2.1.3\t {} / {}\n".format(score, max_score)
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


def q4(svndir, max_score):
    # init return values
    score = 0
    message = ""
    filepath = "{}/4.2.1.4.txt".format(svndir)
    username = None

    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        submitted = read_lines(filepath)
        num_line = len(submitted)
        if num_line == 2:
            username = submitted[0]
            password = submitted[1]
            if len(password) != 20:
                message += "\t+{} login credentials: fail - password length should be 20\n".format(0)
            elif check_cred(username, password):
                score += 20
                message += "\t+{} login credentials: pass\n".format(20)
            else:
                message += "\t+{} login credentials: fail - mismatch\n".format(0)
        else:
            message += "\t+{} login credentials: fail - 1 username and 1 password expected\n".format(0)

    header = "4.2.1.4\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score, username


# validate secret message
def check_secret(username, submitted, student):
    score = 0
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
            score += 5
            message += "\t+{} secret message: pass\n".format(5)
            if username is None or (data['user']['name'] != username):
                message += "\t+{} username match: fail - {} != {}\n".format(0, data['user']['name'], username)
            else:
                score += 5
                message += "\t+{} username match: pass\n".format(5)
        except (ValueError, TypeError):
            message += "\t+{} secret message: fail - unable to decrypt\n".format(0)
    else:
        message += "\t+{} secret message: fail - no secret message found\n".format(0)
    return score, message


def q5(svndir, username, student, max_score):
    # init return values
    score = 0
    message = ""
    filepath = "{}/4.2.1.5.txt".format(svndir)

    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        case_sensitive = True
        submitted = read_lines(filepath, case_sensitive)
        (score, message) = tuple(map(operator.add, (score, message),
                                     check_secret(username, submitted, student)))

    header = "4.2.1.5\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


def q6(svndir, solutions, max_score):
    sol = solutions["year"]
    message = ""
    score = 0
    filepath = "{}/4.2.1.6.txt".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        # start grading
        submitted = read_lines(filepath)
        if (len(submitted) == 1) and (submitted[0] == sol):
            score += 2
            message += "\t+{} number of years in jail: pass\n".format(2)
        else:
            message += "\t+{} number of years in jail: fail\n".format(0)

    header = "4.2.1.6\t {} / {}\n".format(score, max_score)
    return header + message, score, max_score


message_list = dict()
key_message = "show me the money operation cwal"
key_password = "power overwhelming black sheep wall"


def grade_mp4cp2part1(svndir, solution_path, student):
    json_data = open(solution_path).read()
    sol = json.loads(json_data)

    message = ""
    score = 0
    total = 0
    (message, score, total) = tuple(map(operator.add, (message, score, total), q1(svndir, sol, 10)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q2(svndir, sol, 6)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q3(svndir, sol["protocol"], 12)))
    q4_message, q4_score, q4_total, username = q4(svndir, 20)
    (message, score, total) = tuple(map(operator.add, (message, score, total), (q4_message, q4_score, q4_total)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q5(svndir, username, student, 10)))
    (message, score, total) = tuple(map(operator.add, (message, score, total), q6(svndir, sol, 2)))
    header = "4.2.1\t {} / {}\n".format(score, total)

    return header + message, score, total, message_list
