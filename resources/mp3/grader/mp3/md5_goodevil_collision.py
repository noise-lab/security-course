import sys, os, inspect, subprocess
from string import whitespace
from pymd5 import md5, padding
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
filepath1 = "sol_3.2.3_good.py"
filepath2 = "sol_3.2.3_evil.py"
if not (os.path.exists(filepath1) and os.path.exists(filepath2)):
	print "0\tUnable to find your solution file.  Aborting.";
elif crypto_gen_tools.is_empty(filepath1) and crypto_gen_tools.is_empty(filepath2):
    print "0\tSolution files are empty. Aborting."
else:
	# init return values
	score = 0
	message = ''
	default_md5 = "d41d8cd98f00b204e9800998ecf8427e"	# md5(blank file)

    # check solution
	with open(filepath1, "r") as good_file:
		with open(filepath2, "r") as evil_file:
			good_file_content = good_file.read()
			evil_file_content = evil_file.read()
			good_md5 = md5(good_file_content).hexdigest()
			evil_md5 = md5(evil_file_content).hexdigest()
			
			goodfilepath = os.path.join(os.getcwd(), filepath1)
			evilfilepath = os.path.join(os.getcwd(), filepath2)
			good_out = subprocess.check_output(["python", goodfilepath])
			evil_out = subprocess.check_output(["python", evilfilepath])
			
			if (good_md5 == evil_md5 and good_md5 != default_md5):
				message = "\n3.2.3 MD5 *Passed*\n"

				if ('peace' in good_out.rstrip().lower() and 'destroyed' in evil_out.rstrip().lower()):
					message += "\n3.2.3 Output *Passed*\n"
					score = score + 20
				else:
					message += "\n3.2.3 Output *Failed*\n"
			else:
				message = "\n3.2.3 MD5 *Failed*\n"
				
	print str(score) + "\t" + message;
	print "MD5 of good.py, evil.py: " + good_md5 + ", " + evil_md5 + "\n"
	print "Output of good.py: " + good_out.rstrip()
	print "Output of evil.py: " + evil_out.rstrip()
