### Adapted from pre-2010 CS232 Grading script
###
### Tested with Python2.7.2, requires at least 2.7

### Modified 8/30/2014 for CS461 by chuench1
### Note: 
###   The duedate in description file should be the day after the actual due date
###   e.g. if assignment is due 11:59p on Sep 17th, then put Sep 18th
###
###   Check for correctness and manually svn commit after script completed

### Huge refactoring to be use solely for Crypto MP for CS461

import sys, os, time, string, math, glob, threading, re, subprocess, shlex
from datetime import datetime,timedelta
from collections import defaultdict
from pathlib import Path

svn_args = ""
curr_time = datetime.now().strftime("%Y%m%d_%H%M%S")

# python grade.py <svn_basedir> <description_file>

# What's the due date?
# tuple(year, month, day, hour, minute, second, wday(0), yday(0), isdst(0)

def read_description(infile):
	'''
	Read the description file
	'''
	script_dir = os.path.dirname(infile)
	# First line is the mp name, the mp directory name, and due date
	f=open(infile)
	lines=f.readlines()
	mp_name, svndir, duestr = lines[0].rstrip().split('\t')

	# The rest is one test case per lines
	tests={}
	test_names=[]
	duedate=datetime.strptime(duestr, '%m/%d/%Y %I:%M%p')
	total_grade = 0
	for line in lines[1:]:
		#ignore comment
		if line[0] == "#":
			continue
		line=line.rstrip()
		# name -> test name
		# total -> total point possible
		# script -> script file location
		name, total, script_name = line.split('\t')
		script_file_path = str(Path(script_dir)/script_name)
		tests[name] = (int(total),script_file_path)
		test_names.append(name)
		total_grade += int(total)

	return(mp_name, svndir, duedate, tests, test_names, total_grade)


def main():
	# exit immediately if missing arguments
	if (len(sys.argv) < 3):
		print 'usage: python ./grade.py <svn base directory> <description file> <roster file>'
		exit(0)

	svn_basedir = str(Path(sys.argv[1]).resolve())
	description = str(Path(sys.argv[2]).resolve())
	roster_file = str(Path(sys.argv[3]).resolve())
	curr_time = datetime.now().strftime('%Y%m%d_%H%M%S')

	# tests -> map test_name to (total points,script location)
	name, svndir, duedate, tests, test_names, total_grade = read_description(description)

	# instructor grade report file
	instr_report_file = open('{}_grades_{}.txt'.format(name, curr_time), 'w', 0)

	# histogram
	hist = defaultdict(int)

	# grade everyone in roster file
	for netid in open(roster_file):

		############### HACKED IN ######################

		os.system('rm -r /home/thasphon/sp16-ece422/_class/_private/mp3/grader/mp3/test_resources')
		os.system('cp -r /home/thasphon/sp16-ece422/_class/_private/mp3/grader/mp3/orig_test_resources /home/thasphon/sp16-ece422/_class/_private/mp3/grader/mp3/test_resources')

		################################################
		netid = netid.rstrip() 
		work_dir = '{}/{}/{}'.format(svn_basedir, netid, svndir)
		print 'Grading {}'.format(netid)
		grade, comment = grade_student(work_dir, netid, tests, test_names, svn_basedir, duedate)
		
		# update histogram
		hist[grade] += 1
		grade_report(work_dir, netid, grade, comment, total_grade)
		partners = [netid]
		try:
			with open(work_dir + '/partners.txt') as f:
				content = f.readlines()
				if content == []:
					partners = [netid]
				else:
					partners = content
		except:
			pass

		for partner in partners:
			if not partner.strip():
				continue
			partner_report = '{},{}\n'.format(partner.strip(), grade)
			instr_report_file.write(partner_report)

	for score in sorted(hist):
		instr_report_file.write('{}: {}\n'.format(score, hist[score]))
	instr_report_file.close()


def svn_checkout(date):
	'''
	called from grade_student
	update the directory to the latest version before due date

	Due: Not currently using because it makes the script runs really slowly.
	Manually update the repo to the correct timestamp before running the script.
	'''
	p=re.compile(".*?revision (\d+).*?")
	date_str=datetime.strftime(date,"%Y-%m-%d %H:%M")
	svn_cmd="svn "+svn_args+" up -r {\""+date_str+"\"} --accept mine-conflict > svn_out"
	os.system(svn_cmd)
	revision="None"
	for line in open("svn_out"):
		m=p.match(line)
		if m:
			revision=m.group(1)
	return revision


def grade_report(directory, student, grade, comment, total_grade):
	'''
	write and 'svn add' the report file
	'''
	if not os.path.isdir(directory):
		return

	old_path=os.getcwd()
	os.chdir(directory)
	report_path = 'grade_report_{}.txt'.format(curr_time)
	# report_path = 'grade_report_{}.txt'.format('20160314_194037')	
	with open(report_path, 'w') as f:
		grade_string = '{} total : {}/{}\n{}'.format(student, grade, total_grade, comment)
		f.write(grade_string)

	print "svn add "+report_path
	os.system("svn add "+report_path)
	os.chdir(old_path)


def grade_student(directory, netid, tests, test_names, base, duedate):
	'''
	called from main: grade a student
	'''
	# change to student's mp directory; return immediately if not found
	if not os.path.isdir(directory):
		return (0,"mp directory not found\n") 

	old_path=os.getcwd()
	os.chdir(directory)
	print "Changed to directory:"+directory

	best_grade = -1
	best_string = ""
	best_waiver_grade = -1
	lateness = 0
	rv = (0, "Grading script failed.\n")

	overall, possible, gradestring = grade_student_script(directory, netid, tests, test_names, base)
	total_grade = int(round(overall))

	rv = (total_grade,gradestring)
	os.chdir(old_path)
	return rv


def grade_student_script(directory, netid, tests, test_names, base):
	'''
	called from grade_student
	grade the student's submission
	'''
	overall = 0.0
	total_possible = 0.0
	gradestring = ""

	for test_name in test_names:

		# create dump files for graders
		os.system('touch ./tmp ./dump')

		(total, script_path) = tests[test_name] # get total points and script location
		print "\tBeginning test :\t{}".format(test_name)
		print "\tExecuting script:\t{}".format(script_path)

		# run the test script. for my particular test script, need to pass in 
		# svn base directory and netid for expected answer generation
		stdout, err, stderr = run_problem("python {} {} {}".format(script_path, base, netid))
		print stdout, err, stderr

		splitout = stdout.split("\t")
		try:
			sub_grade = float(splitout[0]) # first item is grade
			if len(splitout) > 1:          # and the rest are comments
				comment = '\n'.join(splitout[1:])
			else:
				comment = ''
		except:
			sub_grade = 0
			comment = "Malformed output from subgrader, stdout="+str(stdout)+"\nstderr="+str(stderr)


		gradestring += "{}\t{}/{}\t{}\n\n".format(test_name, sub_grade, total, comment)
		overall += sub_grade
		if test_name.find('bonus') == -1: # bonus part does not increase total possible
			total_possible += total

		# remove dump files 
		os.system('rm ./tmp ./dump')


	return overall, total_possible, gradestring


def run_problem(script):
	'''
	wrapper for run
	run one testcase
	script - the testcase's script location
	'''
	global pid, is_err
	is_err = 0

	(rc, student_stdout, student_stderr) = run(script, shell = True, timeout = 180)

	# if test script time out [not the case for mp1]
	if rc ==-9:
		is_err = 1
		return "0", 1, ""

	student_output = student_stdout.rstrip()
	student_error = student_stderr.split("\n")

	return student_output, is_err, student_error


from os import kill
from signal import alarm, signal, SIGALRM, SIGKILL
from subprocess import PIPE, Popen

def run(args, cwd = None, shell = False, kill_tree = True, timeout = -1, env = None):
    '''
    Run a test script with a timeout after which it will be forcibly
    killed.
    '''
    # empty class and empty handler
    class Alarm(Exception): 
        pass

    def alarm_handler(signum, frame):
        raise Alarm

    # run test script in new process
    p = Popen(args, shell = shell, cwd = cwd, stdout = PIPE, stderr = PIPE, env = env)
    if timeout != -1: # set timeout alarm callback
        signal(SIGALRM, alarm_handler) 
        alarm(timeout)

    try: # wait for process termination and read output
        stdout, stderr = p.communicate() 
        if timeout != -1:
            alarm(0) # cancel alarm if new process terminate in time

    except Alarm: # catch exception: new process timeout
        pids = [p.pid]
        # kill all child processes
        if kill_tree:
            # pids.extend(get_process_children(p.pid))
            pids.extend(get_all_children(p.pid))
        for pid in pids:
            # process might have died before getting to this line
            # so wrap to avoid OSError: no such process
            try: 
                kill(pid, SIGKILL)
            except OSError:
                pass
        return -9, '', '' # if timeout return this
    return p.returncode, stdout, stderr # normal termination return this


def get_all_children(pid):
	'''
	recursively get all descendents processes of pid
	'''
	children = set([pid])
	while(True):
		new_children = []
		for child in children:
			new_children.extend(get_process_children(child))
		new_children = set(new_children)
		if len(new_children - children) == 0:
			break
		children = new_children

	return list(children)
	

def get_process_children(pid):
	'''
	helper function of get_all_children
	return array of  process ids that are children of pid
	'''
	p = Popen('ps --no-headers -o pid --ppid %d' % pid, shell = True, stdout = PIPE, stderr = PIPE)
	stdout, stderr = p.communicate()
	return [int(p) for p in stdout.split()]


if __name__ == '__main__':
	main()
