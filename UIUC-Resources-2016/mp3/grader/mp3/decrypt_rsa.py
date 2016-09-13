import sys, os, inspect, subprocess
from string import whitespace
from pathlib import Path

THIS_SCRIPT_DIR = os.path.dirname(__file__)
sys.path.insert(0, str(Path(THIS_SCRIPT_DIR)/'..'/'..'/'file_generator'))
import crypto_gen_tools

def get_base_16_answer(data):
    ret = -1
    try:
        ret = int(data, 16)
    except ValueError:
        pass
    return ret

# look for solution file
hex_path = "./sol_3.1.2.4.hex"
script_path = "./sol_3.1.2.4.py"
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
    correct_answer = int(crypto_gen_tools.get_prime(netid, extra=crypto_gen_tools.DECRYPT_RSA_EXTRA))

    data = crypto_gen_tools.read_student_solution(hex_path, strip_L = True)
    student_answer = get_base_16_answer(data)
    if(student_answer == correct_answer):
        message += "\n3.1.2.4.hex *Passed*\n"
        score += 1
    else:
        message += "\n3.1.2.4.hex *Failed*\n"
        message += "submission : {}\n".format(student_answer)
        message += "expected   : {}\n".format(correct_answer) 
    # grade script
    dump_file_path = open('./dump', 'wb')
    output_file_path = './tmp'
    test_cipher_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/3.1.2.4_RSA_ciphertext.hex')
    test_key_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/3.1.2.4_RSA_private_key.hex')
    test_mod_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/3.1.2.4_RSA_modulo.hex')
    expected_output_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/sol_3.1.2.4.hex')

    subprocess.call(['python', script_path, test_cipher_path, test_key_path, test_mod_path, output_file_path], stdout=dump_file_path, stderr=dump_file_path)
    output = crypto_gen_tools.read_student_solution(output_file_path, strip_L = True)
    expected_output = crypto_gen_tools.read_student_solution(expected_output_path)

    if(get_base_16_answer(output) == int(expected_output,16)):
        message += "\n3.1.2.4.py *Passed*\n"
        score += 2
    else:
        message += "\n3.1.2.4.py *Failed*\n"    
        message += "submission : {}\n".format(output)
        message += "expected   : {}\n".format(expected_output) 

    print str(score) + "\t" + message
   