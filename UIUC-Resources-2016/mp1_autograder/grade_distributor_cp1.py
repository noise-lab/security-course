import sys
import os

# distribute grades to students in svn.

def svn_add(path):
    os.system('svn add ' + path)

svn_root = "/home/ubuntu/Desktop/sp16-ece422/"
filename = "/home/ubuntu/Desktop/cp1_processed_grades.txt"
with open(filename) as f:
	for line in f:
		line = line.strip()
		netid = line[:line.find(',')]
		path = svn_root+netid+'/mp1/checkpoint1_grade.txt'
                #path = svn_root+"../test.txt"
		lst = line.split(',')
		grade_string  = "MP1 checkpoint 1 grade for "+netid+ " (partner: "+lst[1].strip()+")\n\n"
		grade_string += "1.1.1_addr  : " + lst[2].strip() +"/2\n"
                grade_string += "Comment : " + lst[3].strip() + "\n\n"
		grade_string += "1.1.1_eax  : " + lst[4].strip() +"/2\n"
                grade_string += "Comment : " + lst[5].strip() + "\n\n"
		grade_string += "1.1.2  : " + lst[6].strip() +"/4\n"
                grade_string += "Comment : " + lst[7].strip() + "\n\n"
		grade_string += "1.1.3  : " + lst[8].strip() +"/4\n"
                grade_string += "Comment : " + lst[9].strip() + "\n\n"
		grade_string += "1.1.4  : " + lst[10].strip() +"/4\n"
                grade_string += "Comment : " + lst[11].strip() + "\n\n"
		grade_string += "1.1.5  : " + lst[12].strip() +"/4\n"
                grade_string += "Comment : " + lst[13].strip() + "\n\n"
		grade_string += "total   : " + lst[14].strip() +"/20\n"

                #with open(svn_root+"/../sample.txt","a") as p:
                if os.path.exists(path):
                    os.remove(path)
		with open(path,"a") as p:
                    p.write(grade_string)
	        svn_add(path)
