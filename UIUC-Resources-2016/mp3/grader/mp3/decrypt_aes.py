import sys, os, inspect, subprocess
from string import whitespace
from pathlib import Path

THIS_SCRIPT_DIR = os.path.dirname(__file__)
sys.path.insert(0, str(Path(THIS_SCRIPT_DIR)/'..'/'..'/'file_generator'))
import crypto_gen_tools

def countDiffChars(s1, s2):
    count = 0
    for i in range(min(len(s1),len(s2))):
        if(s1[i]!=s2[i]):
            count+=1
    return count+abs(len(s1)-len(s2))

# look for solution file
txt_path = "./sol_3.1.2.2.txt"
script_path = "./sol_3.1.2.2.py"
if not (os.path.exists(txt_path) and os.path.exists(script_path)):
    print "0\tUnable to find your solution file.  Aborting."
elif crypto_gen_tools.is_empty(txt_path) and crypto_gen_tools.is_empty(script_path):
    print "0\tSolution files are empty. Aborting."
else:
    # init return values
    score = 0
    message = ''

    # grade txt
    netid = sys.argv[2]
    plaintext_orig = crypto_gen_tools.get_jeopardy_line(netid, extra=crypto_gen_tools.DECRYPT_AES_EXTRA)
    plaintext = plaintext_orig.translate(None, whitespace)
    plaintext = crypto_gen_tools.uppercase_sanitize(plaintext)

    data = crypto_gen_tools.read_student_solution(txt_path)
    if(data == plaintext or countDiffChars(data,plaintext) < 0.05*len(plaintext)):
        message += "\n3.1.2.2.txt *Passed*\n"
        score += 1
    else:
        message += "\n3.1.2.2.txt *Failed*\n"
        message += "submission : {}\n".format(data)
        message += "expected   : {}\n".format(plaintext)        

    # grade script
    dump_file_path = open('./dump', 'wb')
    output_file_path = './tmp'
    test_cipher_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/3.1.2.2_aes_ciphertext.hex')
    test_key_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/3.1.2.2_aes_key.hex')
    test_iv_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/3.1.2.2_aes_iv.hex')
    expected_output_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/sol_3.1.2.2.txt')

    subprocess.call(['python', script_path, test_cipher_path, test_key_path, test_iv_path, output_file_path], stdout=dump_file_path, stderr=dump_file_path)
    output = crypto_gen_tools.read_student_solution(output_file_path)
    expected_output = crypto_gen_tools.read_student_solution(expected_output_path)
    if(output == expected_output):
        message += "\n3.1.2.2.py *Passed*\n"
        score += 2
    else:
        message += "\n3.1.2.2.py *Failed*\n"
        message += "submission : {}\n".format(output)
        message += "expected   : {}\n".format(expected_output)     

    print str(score) + "\t" + message
    