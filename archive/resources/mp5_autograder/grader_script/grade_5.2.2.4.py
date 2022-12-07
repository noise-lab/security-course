import os
import tools
from string import whitespace
# import Crypto.Hash.SHA256 as SHA256
import hashlib

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

def get_suspect_selection(filepath):
    with open(filepath, 'r') as f:
        line = f.read().strip()
        suspect = line[len(line)-1]
    return suspect

# solution
l_sol = ['hackers']
w_sol = ['aborted']

sol = {'1' : l_sol,
       '3' : w_sol}

decryptfile_hash_l = "../../_class/_private/mp5/solution/password_hash_l.txt"
decryptfile_hash_l_2 = "../../_class/_private/mp5/solution/password_hash_l_2.txt"
decryptfile_hash_w = "../../_class/_private/mp5/solution/password_hash_w.txt"
decryptfile_hash_w_2 = "../../_class/_private/mp5/solution/password_hash_w_2.txt"

hash_l_sol = ""
with open(decryptfile_hash_l) as f:
    hash_l_sol = f.read().strip()

hash_l_2_sol = ""
with open(decryptfile_hash_l_2) as f:
    hash_l_2_sol = f.read().strip()

hash_w_sol = ""
with open(decryptfile_hash_w) as f:
    hash_w_sol = f.read().strip()

hash_w_2_sol = ""
with open(decryptfile_hash_w_2) as f:
    hash_w_2_sol = f.read().strip()

hash_l_sol_list = [hash_l_sol, hash_l_2_sol]
hash_w_sol_list = [hash_w_sol, hash_w_2_sol]

hash_sol = {'1' : hash_l_sol_list,
            '3' : hash_w_sol_list}

# look for solution file
password_filepath = "./5.2.2.4.txt"
evidence_filepath = "./evidence/"
decryptfile_filepath = "./evidence/password.txt"
compressfile_filepath = "./evidence/password.zip"

if not (os.path.exists(password_filepath)):
    print "0\tUnable to find your solution file(s).  Aborting.\n"
else:
    # init return values
    score = 0
    message = "\n"

    # suspect selection
    suspect_path = "./suspect_vm.txt"
    suspect = get_suspect_selection(suspect_path)

    # start grading
    password_submission = read_solution(password_filepath)

    # grade encrypt password
    for ps in sol[suspect]:
        if ps in password_submission:
            score += 5
            message += "password passed\n"
        else:
            message += "password failed\n"

    # grade decrypt file evidence
    if not os.path.exists(decryptfile_filepath):
        message += "file doesn't exist or file name or format doesn't match\n"
    else:
        # compare the checksum of the files
        hash_submission = hashlib.md5(open(decryptfile_filepath, 'rb').read()).hexdigest()

        if hash_submission in hash_sol[suspect]:
            score += 5
            message += "decrypted file passed\n"
        else:
            message += "file does not match\n"
        
    # print result
    print str(score) + "\t" + message
