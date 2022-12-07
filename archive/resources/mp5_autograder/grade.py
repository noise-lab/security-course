### Adapted from pre-2010 CS232 Grading script
###
### Tested with Python2.7.2, requires at least 2.7

### Modified 8/30/2014 for CS461 by chuench1
### Note: 
###   The duedate in description file should be the day after the actual due date
###   e.g. if assignment is due 11:59p on Sep 17th, then put Sep 18th
###
###   Check for correctness and manually svn commit after script completed


import sys, os, time, string, math, glob, threading,re;
from datetime import datetime,timedelta;
import subprocess, shlex;
from collections import defaultdict

svn_args="";
curr_time = datetime.now().strftime("%Y%m%d_%H%M%S")

# python grade.py <svn_basedir> <description_file>

# What's the due date?
# tuple(year, month, day, hour, minute, second, wday(0), yday(0), isdst(0)

def read_description(infile):
	'''
	Read the description file
	'''
	f=open(infile);

	# First line is the mp name, the mp directory name, and due date
	lines=f.readlines();
	(mp_name,svndir,duestr)=lines[0].rstrip().split('\t');

	# The rest is one test case per lines
	tests={};
	test_names=[];
	duedate=datetime.strptime(duestr+" 06:00PM", '%m/%d/%Y %I:%M%p')
	total_grade = 0
	for line in lines[1:]:
		#ignore comment
		if line[0]=="#":
			continue;
		line=line.rstrip();
		# name -> test name
		# total -> total point possible
		# script -> script file location
		name,total,script=line.split('\t');
		tests[name]=(int(total),script);
		test_names.append(name);
		total_grade += int(total)
	return(mp_name,svndir,duedate,tests,test_names, total_grade);


def main():
	# exit immediately if missing arguments
	if (len(sys.argv) < 3):
		print "usage: python ./grade.py <svn base directory> <description file>"
		exit(0)

	svn_basedir = sys.argv[1];
	description = sys.argv[2];
	curr_time = datetime.now().strftime("%Y%m%d_%H%M%S")

	# tests -> map test_name to (total points,script location)
	(name,svndir,duedate,tests,test_names, total_grade)=read_description(description);

	# instructor grade report file
	gr=open(name+"_grades_"+str(curr_time)+".txt","w",0);

	# histogram
	hist = defaultdict(int)

	# grade everyone in roster file
	# for student in open(svn_basedir+"/_rosters/students.txt"):
	# for student in open(svn_basedir+"/_class/_private/extensions/mp5cp2_extension_list.txt"):
	for student in open(svn_basedir+"/_rosters/meonly.txt"):
		student=student.rstrip(); # netid
		print "Grading "+student;
		(grade,comment)=grade_student(svn_basedir+"/"+student+"/"+svndir,student,tests,test_names,svn_basedir,duedate);
		# update histogram
		hist[grade] += 1
		# grade_report(svn_basedir+"/"+student+"/"+svndir,student,grade,comment, total_grade);
		partners = [student]
		try:
			with open(svn_basedir+"/"+student+"/"+svndir+"/partners.txt") as f:
				content = f.readlines()
				if content == []:
					partners = [student]
				else:
					partners = content
		except:
			pass

		for partner in partners:
			partner = partner.strip()
			if partner == '':
				break # continue
			gr.write("\""+partner+"\"\t\""+str(grade)+"\"\n")
			grade_report(svn_basedir+"/"+partner+"/"+svndir,partner,grade,comment, total_grade)
	for score in sorted(hist):
		gr.write('{}: {}\n'.format(score, hist[score]))
	gr.close();

def svn_checkout(date):
	'''
	called from grade_student
	update the directory to the latest version before due date

	Due: Not currently using because it makes the script runs really slowly.
	     Update the repo to the correct timestamp before running the script.
	'''
	p=re.compile(".*?revision (\d+).*?");
	date_str=datetime.strftime(date,"%Y-%m-%d %H:%M");
	svn_cmd="svn "+svn_args+" up -r {\""+date_str+"\"} --accept mine-conflict > svn_out"
	os.system(svn_cmd);
	revision="None";
	for line in open("svn_out"):
		m=p.match(line);
		if m:
			revision=m.group(1);
	return revision;


def grade_report(directory,student,grade,comment, total_grade):
	'''
	write and 'svn add' the report file
	'''
	# return immediately if directory is not found
	if not os.path.isdir(directory):
		return;	

	oldpath=os.getcwd();
	os.chdir(directory)
	# open and write new report file
	report_fname="grade_report_"+curr_time+".txt"
	fh=open(report_fname,'w');
	grade_string=student+" total : "+str(grade)+"/" + str(total_grade) + "\n"
	grade_string+=comment;
	fh.write(grade_string);
	fh.close();
	# add to svn
	# print "svn add "+report_fname
	# os.system("svn add "+report_fname);
	os.chdir(oldpath);


def grade_student(directory, netid, tests,test_names,base,duedate):
	'''
	called from main: grade a student
	'''
	# change to student's mp directory; return immediately if not found
	oldpath=os.getcwd();
	if not os.path.isdir(directory):
		return (0,"No lab directory found\n") 
	os.chdir(directory);
	print "Changed to directory:"+directory;

	best_grade=-1;
	best_string="";
	best_waiver_grade=-1;
	lateness=0;
	rv=(0,"Grading script failed.\n");
	prev_revision=None;

	(overall,possible,gradestring)=grade_student_script(directory,netid,tests,test_names,base);
	total_grade=overall

	rv=(total_grade,gradestring);
	os.chdir(oldpath);
	return rv;


def grade_student_script(directory,netid,tests,test_names,base):
	'''
	called from grade_student
	grade the student's submission
	'''
	overall=0.0;
	possible=0;
	gradestring="";
	# for each tests
	for test_name in test_names:
		(total,script)=tests[test_name]; # get total points and script location

		print "\tBeginning test :\t"+test_name;
		print "\tExecuting script:\t"+base+"/"+script;
		# run the test script. for my particular test script, need to pass in 
		# svn base directory and netid for expected answer generation
		(stdout,err,stderr)=run_problem("python "+base+"/"+script+" "+base+" "+netid);
		print stdout, err, stderr;
		splitout=stdout.split("\t");
		sub_grade=0;
		comment="";
		# get grade information from stdout
		try:
			sub_grade=float(splitout[0]);
		# cannot parse grade value to int
		except ValueError:
			comment="ValueError running code:";
			comment+=stdout;
			comment+=str(stderr);
		# if grading script does not terminate correctly [not the case for mp1]
		if err!=0:
			sub_grade=0;
			comment="Error running code:";
			comment+=stdout;
			comment+=str(stderr);
		# add the rest of grading script output to comments
		if len(splitout)>1:
			for spl in splitout[1:]:
				comment+=spl+"\n";
		# append to the final output
		gradestring+=test_name+"\t"+str(sub_grade)+"/"+str(total)+"\t"+comment+"\n\n";
		# bonus does not contribute to total possible score
		if test_name.find('bonus') == -1:
			possible+=total;
		overall+=sub_grade;
	return overall,possible,gradestring;


def run_problem(script):
	'''
	wrapper for run
	run one testcase
	script - the testcase's script location
	'''
	global pid, is_err
	is_err = 0

	(rc,student_stdout,student_stderr)=run(script, shell = True, timeout = 120)

	# if test script time out [not the case for mp1]
	if rc ==-9:
		is_err = 1
		return ("0", 1, "")

	student_output = student_stdout.rstrip();
	student_error = student_stderr.split("\n")

	return (student_output, is_err, student_error)


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
        signal(SIGALRM, alarm_handler) # set handler
        alarm(timeout)	# activate countdown

    try:
    	# wait for process termination and read output
        stdout, stderr = p.communicate() 
        if timeout != -1:
            alarm(0) # cancel alarm if new process terminate in time

    except Alarm: # catch exception: new process timeout
        pids = [p.pid]
        # kill all child processes
        if kill_tree:
            #pids.extend(get_process_children(p.pid))
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
	recursively get all heirs(child) processes of pid
	'''
	children=set([pid]);
	while(True):
		new_children=[];
		for child in children:
			new_children.extend(get_process_children(child));
		new_children=set(new_children);
		if len(new_children-children)==0:
			break;
		children=new_children;
	return list(children);
	

def get_process_children(pid):
	'''
	helper function of get_all_children
	return array of  process ids that are children of pid
	'''
	p = Popen('ps --no-headers -o pid --ppid %d' % pid, shell = True, stdout = PIPE, stderr = PIPE)
	stdout, stderr = p.communicate()
	return [int(p) for p in stdout.split()]

main();
