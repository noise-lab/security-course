import sys, os, inspect, subprocess, urllib
from string import whitespace
from pathlib import Path
from pymd5 import md5, padding

THIS_SCRIPT_DIR = os.path.dirname(__file__)
sys.path.insert(0, str(Path(THIS_SCRIPT_DIR)/'..'/'..'/'file_generator'))
import crypto_gen_tools

txt_path = "./sol_3.2.1.2.txt"
script_path = "./sol_3.2.1.2.py"
if not (os.path.exists(txt_path) and os.path.exists(script_path)):
    print "0\tUnable to find your solution file.  Aborting."
elif crypto_gen_tools.is_empty(txt_path) and crypto_gen_tools.is_empty(script_path):
    print "0\tSolution files are empty. Aborting."
else:
    # init return values
    score = 0
    message = ''

    # get solution
    netid = sys.argv[2]
    student_hash = crypto_gen_tools.get_student_hash(netid)
    password = crypto_gen_tools.generate_student_password(student_hash)
    command = "user=admin&command1=ListFiles&command2=NoOp"
    attack = "&command3=DeleteAllFiles"
    pad_len = len(password + command)
    new_command = command + padding(pad_len*8) + attack
    token = md5(password + new_command).hexdigest()
    query = 'token=' + token + '&' + new_command

    new_command_quote = command + urllib.quote(padding(pad_len*8)) + attack
    query_quote = 'token=' + token + '&' + new_command_quote

    data = crypto_gen_tools.read_student_solution(txt_path, uppercase_sanitized = False)
    data_unquoted = urllib.unquote(data)

    if data_unquoted == query or data == query_quote or query in data_unquoted:
        message += '\n3.2.1.2.txt *Passed*\n'
        score += 5
    elif token in data:
        message += '\n3.2.1.2.txt - wrong padding\n'
        score += 2.5

    message += "submission : {}\n".format(data)
    message += "expected   : {}\n".format(query_quote) 

    # grade script
    dump_file_path = open('./dump', 'wb')
    output_file_path = './tmp'
    test_query_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/3.2.1.2_query.txt')
    test_cmd3_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/3.2.1.2_command3.txt')
    expected_output_path = str(Path(THIS_SCRIPT_DIR)/'test_resources/sol_3.2.1.2.txt')

    subprocess.call(['python', script_path, test_query_path, test_cmd3_path, output_file_path], stdout=dump_file_path, stderr=dump_file_path)
    output = crypto_gen_tools.read_student_solution(output_file_path, uppercase_sanitized = False)
    expected_output = crypto_gen_tools.read_student_solution(expected_output_path, uppercase_sanitized = False)
    if(urllib.unquote(output) == urllib.unquote(expected_output) or urllib.unquote(expected_output) in urllib.unquote(output)):
        message += "\n3.2.1.2.py *Passed*\n"
        score += 15
    elif '5d4d80e28ab8792eb88ae6471224b1fe' in output:
        message += "\n3.2.1.2.py *Wrong Padding*\n"
        message += "submission : {}\n".format(urllib.unquote(output))
        message += "expected   : {}\n".format(urllib.unquote(expected_output))
        score += 7.5
    else:
        message += "\n3.2.1.2.py *Failed*\n"
        message += "submission : {}\n".format(urllib.unquote(output))
        message += "expected   : {}\n".format(urllib.unquote(expected_output)) 
        
    print str(score) + "\t" + message