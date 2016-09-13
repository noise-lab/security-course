import sys, os, inspect, subprocess
from string import whitespace
from pathlib import Path
from Crypto.Hash import SHA256

THIS_SCRIPT_DIR = os.path.dirname(__file__)
sys.path.insert(0, str(Path(THIS_SCRIPT_DIR)/'..'/'..'/'file_generator'))
import crypto_gen_tools

def compute_hash(text):
    h = SHA256.new()
    h.update(text)
    return int(h.hexdigest(),16)

def get_base_16_answer(data):
    ret = -1
    try:
        ret = int(data, 16)
    except ValueError:
        pass
    return ret

# look for solution file
hex_path = "./sol_3.1.3.1.hex"
script_path = "./sol_3.1.3.1.py"
if not (os.path.exists(hex_path) and os.path.exists(script_path)):
    print "0\tUnable to find your solution file.  Aborting."
elif crypto_gen_tools.is_empty(hex_path) and crypto_gen_tools.is_empty(script_path):
    print "0\tSolution files are empty. Aborting."
else:
    # init return values
    score = 0
    message = ''

    # grade hex
    netid = sys.argv[2]
    plaintext = crypto_gen_tools.get_jeopardy_line(netid, extra=crypto_gen_tools.AVALANCHE_EFFECT_EXTRA)
    plaintext_sanitized = crypto_gen_tools.uppercase_sanitize(plaintext)
    orig_hash = compute_hash(plaintext_sanitized)

    perturbed_string = crypto_gen_tools.flip_a_bit(netid, plaintext)
    perturbed_string = crypto_gen_tools.uppercase_sanitize(perturbed_string)
    perturbed_hash = compute_hash(perturbed_string)

    x_or_string = bin(orig_hash^perturbed_hash)
    count = str(x_or_string).count('1')

    # start grading
    data = crypto_gen_tools.read_student_solution(hex_path, strip_L = True)

    if(int(data, 16) == count):
        message += "\n3.1.3.1.hex *Passed*\n"
        score += 1
    else:
        message += "\n3.1.3.1.hex *Failed*\n"
        message += "submission : {}\n".format(str(int(data,16)))
        message += "expected   : {}\n".format(str(count))


    # grade script
    dump_file_path = open('./dump', 'wb')
    output_file_path = './tmp'
    test_str_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/3.1.3.1_input_string.txt')
    test_mod_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/3.1.3.1_perturbed_string.txt')
    expected_output_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/sol_3.1.3.1.hex')

    subprocess.call(['python', script_path, test_str_path, test_mod_path, output_file_path], stdout=dump_file_path, stderr=dump_file_path)
    output = crypto_gen_tools.read_student_solution(output_file_path, strip_L = True)
    expected_output = crypto_gen_tools.read_student_solution(expected_output_path, strip_L = True)
    if(get_base_16_answer(output) == int(expected_output,16)):
        message += "\n3.1.3.1.py *Passed*\n"
        score += 2
    else:
        message += "\n3.1.3.1.py *Failed*\n" 
        message += "submission : {}\n".format(output)
        message += "expected   : {}\n".format(expected_output)  


    print str(score) + "\t" + message
