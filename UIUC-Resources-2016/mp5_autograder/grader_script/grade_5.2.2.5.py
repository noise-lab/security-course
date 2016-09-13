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
account_l_sol = ['root']
account_w_sol = ['ladiesman461']

account_sol = {'1' : account_l_sol,
               '3' : account_w_sol}

tools_sol = ['nmap', 'hydra']
indirect_attack_tools = []
non_attack_tools = ['aircrack']

ip_l_sol = ['10.46.1.105']
ip_w_sol = ['10.46.1.106', '10.46.1.105']

ip_sol = {'1' : ip_l_sol,
          '3' : ip_w_sol}

connection_sol = ['yes', 'ssh_host_ecdsa_key', 'ssh_host_ecdsa_key.pub']
public_key_sol = ['known_hosts']

password_l_sol = ['sexyboy']
password_w_sol = ['sexyman']

password_sol = {'1' : password_l_sol,
                '3' : password_w_sol}

# look for solution file
account_filepath = "./5.2.2.5_account.txt"
tools_filepath = "./5.2.2.5_tools.txt"
ip_filepath = "./5.2.2.5_ip.txt"
connection_filepath = "./5.2.2.5_connection.txt"
password_filepath = "./5.2.2.5_password.txt"

if not (os.path.exists(account_filepath) and os.path.exists(tools_filepath) and os.path.exists(ip_filepath) and os.path.exists(connection_filepath) and os.path.exists(password_filepath)):
    print "0\tUnable to find your solution file(s).  Aborting."
else:
    # init return values
    score = 0;
    message = "\n";

    # suspect selection
    suspect_path = "./suspect_vm.txt"
    suspect = get_suspect_selection(suspect_path)

    # start grading
    account_submission = read_solution(account_filepath)
    tools_submission = read_solution_string(tools_filepath)
    ip_submission = read_solution(ip_filepath)
    connection_submission = read_solution(connection_filepath)
    password_submission = read_solution_string(password_filepath)

    # grade attack account username: 3 points
    for accs in account_sol[suspect]:
        if accs in account_submission:
            score += 3
            message += accs + " passed\n"
        else:
            message += accs + " failed\n"

    # grade attack tools list: 4 points
    tool_score = 0
    for ts in tools_sol:
        if ts in tools_submission:
            tool_score += 2
            message += ts + " passed\n"
    for nat in non_attack_tools:
        if nat in tools_submission:
            tool_score -= 1
            message += "non attack tool included\n"

    if tool_score <= 0:
        tool_score = 0
    elif tool_score >= 4:
        tool_score = 4
    score += tool_score

    # grade ip address: 2 points
    for ips in ip_sol[suspect]:
        if ips in ip_submission:
            if suspect == '1':
                score += 2
            elif suspect == '3':
                score += 1
            message += ips + " passed\n"
        else:
            message += ips + " failed\n"

    if len(ip_submission) > len(ip_sol[suspect]):
        score -= 1
        message += "submitted too many ip addresses\n"
    if len(ip_submission) < len(ip_sol[suspect]):
        message += "insufficiently listed ip addresses\n"

    # grade connection information: 6 points
    for cs in range(0, len(connection_submission)):
        connection_submission[cs] = connection_submission[cs].lower()
        if connection_submission[cs] == connection_sol[cs]:
            score += 2
            message += connection_submission[cs] + " passed\n"
        elif cs == 0 and connection_submission[cs] == 'successful':
            score += 2
            message += connection_submission[cs] + " passed\n"
        elif cs == 2 and connection_submission[cs] in public_key_sol:
            score += 2
            message += connection_submission[cs] + " passed\n"
        else:
            message += connection_submission[cs] + " failed\n"

    # grade account password: 5 points
    if password_submission in password_sol[suspect]:
        score += 5
        message += "password passed\n"
    else:
        message += "password failed\n"

    # print result
    print str(score)+"\t"+message;
    
