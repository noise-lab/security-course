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
l_sol = ['suicidenote.doc']
w_sol = ['toxic waste 1.7 oz.jpg', 'evilplan.doc']

sol = {'1' : l_sol,
       '3' : w_sol}

deletedfile_hash_l = "../../_class/_private/mp5/solution/suicidenote_hash.txt"
deletedfile_hash_empty_l = "../../_class/_private/mp5/solution/suicidenote_empty_hash.txt"
deletedfile_hash_w = "../../_class/_private/mp5/solution/toxicwaste_hash.txt"
deletedfile_hash_evilplan_w = "../../_class/_private/mp5/solution/evilplan_hash.txt"
deletedfile_hash_thumbnail_w = "../../_class/_private/mp5/solution/toxicwaste_thumbnail_hash.txt"

hash_l_sol = ""
with open(deletedfile_hash_l) as f:
    hash_l_sol = f.read().strip()

hash_l_empty_sol = ""
with open(deletedfile_hash_empty_l) as f:
    hash_l_empty_sol = f.read().strip()

hash_w_sol = ""
with open(deletedfile_hash_w) as f:
    hash_w_sol = f.read().strip()

hash_w_evilplan_sol = ""
with open(deletedfile_hash_evilplan_w) as f:
    hash_w_evilplan_sol = f.read().strip()

hash_w_thumbnail_sol = ""
with open(deletedfile_hash_thumbnail_w) as f:
    hash_w_thumbnail_sol = f.read().strip()

hash_l_sol_list = [hash_l_sol]
hash_l_empty_list = [hash_l_empty_sol]
hash_w_sol_list = [hash_w_sol, hash_w_evilplan_sol, hash_w_thumbnail_sol]

hash_sol = {'1' : hash_l_sol_list,
            '3' : hash_w_sol_list}

# look for solution file
filename_filepath = "./5.2.2.6.txt"
evidence_filepath = "./evidence/"
deletedfile_l_filepath = "./evidence/suicidenote.doc"
deletedfile_w_filepath = "./evidence/toxic waste 1.7 oz.jpg"
deletedfile_w_filepath_evilplan = "./evidence/evilplan.doc"
deletedfile_w_filepath_thumbnail = "./evidence/cd04c9e3bc6428226e230469c27f041e.png"

deletedfile_filepath = {'1' : deletedfile_l_filepath,
                        '3' : deletedfile_w_filepath}

if not (os.path.exists(filename_filepath)):
    print "0\tUnable to find your solution file(s).  Aborting.\n"
else:
    # init return values
    score = 0
    message = "\n"

    # suspect selection
    suspect_path = "./suspect_vm.txt"
    suspect = get_suspect_selection(suspect_path)

    # start grading
    filename_submission = read_solution(filename_filepath)

    # grade deleted filename
    for fs in filename_submission:
        if fs in sol[suspect]:
            score += 5
            message += "filename passed\n"
            break
        else:
            message += "filename failed\n"

    # grade extracted deleted file evidence
    if not (os.path.exists(deletedfile_filepath[suspect]) or os.path.exists(deletedfile_w_filepath_thumbnail) or os.path.exists(deletedfile_w_filepath_evilplan)):
        message += "file doesn't exist or file name doesn't match"
    else:
        correct_filename = True
        df_filepath = deletedfile_filepath[suspect]

        if suspect == 'w':
            if os.path.exists(deletedfile_w_filepath_thumbnail) and not os.path.exists(deletedfile_filepath[suspect]):
                correct_filename = False
                df_filepath = deletedfile_w_filepath_thumbnail
                message += "file name not changed to original\n"
            elif os.path.exists(deletedfile_w_filepath_evilplan):
                df_filepath = deletedfile_w_filepath_evilplan
            else:
                df_filepath = ''
                message += "has not successfully extracted/recovered the file\n"

        # compare the checksum of the files
        hash_submission = 0
        if (df_filepath != ''):
            hash_submission = hashlib.md5(open(df_filepath, 'rb').read()).hexdigest()

        if hash_submission in hash_sol[suspect]:
            score += 5
            message += "deleted file passed\n"
            # if not correct_filename:
            #     score -= 1
        else:
            message += "file does not match\n"
        
    # print result
    print str(score) + "\t" + message
