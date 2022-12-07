import sys, os, inspect
from string import whitespace
from pathlib import Path

THIS_SCRIPT_DIR = os.path.dirname(__file__)
sys.path.insert(0, str(Path(THIS_SCRIPT_DIR)/'..'/'..'/'file_generator'))
import crypto_gen_tools

# look for solution file
filepath1 = "./sol_3.1.1.2_decimal.txt"
filepath2 = "./sol_3.1.1.2_binary.txt"
if not (os.path.exists(filepath1) and os.path.exists(filepath2)):
    print "0\tUnable to find your solution file(s).  Aborting."
elif crypto_gen_tools.is_empty(filepath1) and crypto_gen_tools.is_empty(filepath2):
    print "0\tSolution files are empty. Aborting."
else:
    # init return values
    score = 0
    message = ""

    # get solution
    netid = sys.argv[2]
    integer_answer = crypto_gen_tools.get_student_random_number(netid, extra=crypto_gen_tools.PYTHON_EXERCISE_EXTRA)

    # start grading
    data = crypto_gen_tools.read_student_solution(filepath1)
    if(int(data) == integer_answer):
        message += "\n3.1.1.2_decimal *Passed*\n"
        score += 1.0
    else :
        message += "\n3.1.1.2_decimal *Failed*\n"

    data = crypto_gen_tools.read_student_solution(filepath2)
    if(int(data,2) == integer_answer):
        message += "\n3.1.1.2_binary *Passed*\n"
        score += 1.0
    else :
        message += "\n3.1.1.2_binary *Failed*\n"

    # print result
    print str(score) + "\t" + message
    
