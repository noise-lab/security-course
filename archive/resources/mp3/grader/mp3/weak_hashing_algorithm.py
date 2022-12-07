import sys, os, inspect, subprocess
from string import whitespace
from pathlib import Path
from Crypto.Hash import SHA256

THIS_SCRIPT_DIR = os.path.dirname(__file__)
sys.path.insert(0, str(Path(THIS_SCRIPT_DIR)/'..'/'..'/'file_generator'))
import crypto_gen_tools

def bad_hash(s):
    h=0
    m=0x3FFFFFFF
    for c in s:
        i=ord(c)
        i=((i^0xCC)<<24) |((i^0x33)<<16) | ((i^0xAA)<<8) | (i^0x55)
        h=(h&m)+(i&m)
    return h
def get_base_16_answer(data):
    ret = -1
    try:
        ret = int(data, 16)
    except ValueError:
        pass
    return ret

# look for solution file
txt_path = "./sol_3.1.3.2.txt"
script_path = "./sol_3.1.3.2.py"
if not os.path.exists(txt_path):
    print "0\tUnable to find your solution file.  Aborting."
elif crypto_gen_tools.is_empty(txt_path) and crypto_gen_tools.is_empty(script_path):
    print "0\tSolution files are empty. Aborting."
else:
    # init return values
    score = 0
    message = ''

    # grade txt
    netid = sys.argv[2]
    plaintext = crypto_gen_tools.get_jeopardy_line(netid, extra=crypto_gen_tools.WHA_EXTRA)
    plaintext = crypto_gen_tools.uppercase_sanitize(plaintext)
    orig_hash = bad_hash(plaintext)

    data = crypto_gen_tools.read_student_wha_solution(txt_path)
    student_hash = bad_hash(data)
    if(student_hash == orig_hash and plaintext != data ):
        message += "\n3.1.3.2.txt *Passed*\n"
        score += 1
    else:
        message += "\n3.1.3.2.txt *Failed*\n"
        message += "Given Plaintext: {}\n".format(plaintext)
        message += "Expected hash  : {}\n".format(str(orig_hash))
        message += "Student's text : {}\n".format(data)
        message += "Student's hash : {}\n".format(str(student_hash))
    # grade script
    dump_file_path = open('./dump', 'wb')
    output_file_path = './tmp'
    intput_file_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/3.1.3.2_input_string.txt')

    subprocess.call(['python', script_path, intput_file_path, output_file_path], stdout=dump_file_path, stderr=dump_file_path)
    output = crypto_gen_tools.read_student_solution(output_file_path)
    expected_output = bad_hash('HUSBAND  WIFE ABRAHAM  MAHALA PUT THEIR LAST NAME ON THIS LINE OF FROZEN ENTREES MEATLOAF AGAIN')
    if(get_base_16_answer(output) == expected_output):
        message += "\n3.1.3.2.py *Passed*\n"
        score += 2
    else:
        message += "\n3.1.3.2.py *Failed*\n"
        message += "output   : {}\n".format(output)
        message += "expected : {}\n".format(hex(expected_output).rstrip('L')[2:])   

    print str(score) + "\t" + message