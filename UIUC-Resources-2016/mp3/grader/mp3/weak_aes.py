import sys, os, inspect, subprocess
from string import whitespace
from pathlib import Path

THIS_SCRIPT_DIR = os.path.dirname(__file__)
sys.path.insert(0, str(Path(THIS_SCRIPT_DIR)/'..'/'..'/'file_generator'))
import crypto_gen_tools

# look for solution file
filepath = "./sol_3.1.2.3.hex"
if not os.path.exists(filepath):
    print "0\tUnable to find your solution file.  Aborting."
elif crypto_gen_tools.is_empty(filepath):
    print "0\tSolution files are empty. Aborting."
else:
    # init return values
    score = 0
    message = "\n3.1.2.3 *Failed*\n"

    # get solution
    netid = sys.argv[2]
    student_hash = crypto_gen_tools.get_student_hash(netid)
    weak_aes_key_int = crypto_gen_tools.generate_student_weak_aes_key_int(student_hash)
    weak_aes_key_hex = crypto_gen_tools.generate_student_weak_aes_key(student_hash)
    plaintext = crypto_gen_tools.get_jeopardy_line(netid, extra=crypto_gen_tools.WEAK_AES_EXTRA)

    # start grading
    data = crypto_gen_tools.read_student_solution(filepath)

    if(data == weak_aes_key_hex or int(data,16) == int(weak_aes_key_hex,16)):
        message = "\n3.1.2.3 *Passed*\n"
        score = 3
    else:
        message += "submission : {}\n".format(data)
        message += "expected   : {}\n".format(str(weak_aes_key_hex))
        message += "plaintext  : {}\n".format(plaintext)

    print str(score) + "\t" + message
   