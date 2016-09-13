import sys
import os

# distribute grades to students in svn.
# argv[1] is the csv grade file  

def svn_add(path):
    os.system('svn add ' + path)

svn_root = "/home/ubuntu/Desktop/sp16-ece422/"
filename = "/home/ubuntu/Desktop/cp2_processed_grades.txt"
with open(filename) as f:
	for line in f:
		line = line.strip()
		netid = line[:line.find(',')]
		path = svn_root+netid+'/mp1/checkpoint2_grade.txt'
                #path = svn_root+"../test.txt"
		lst = line.split(',')
		grade_string  = "MP1 checkpoint 2 grade for "+netid+ " (partner: "+lst[1].strip()+")\n\n"
		grade_string += "1.2.1  : " + lst[2].strip() +"/8\n"
                grade_string += "Comment : " + lst[3].strip() + "\n\n"
		grade_string += "1.2.2  : " + lst[4].strip() +"/8\n"
                grade_string += "Comment : " + lst[5].strip() + "\n\n"
		grade_string += "1.2.3  : " + lst[6].strip() +"/8\n"
                grade_string += "Comment : " + lst[7].strip() + "\n\n"
		grade_string += "1.2.4  : " + lst[8].strip() +"/9\n"
                grade_string += "Comment : " + lst[9].strip() + "\n\n"
		grade_string += "1.2.5  : " + lst[10].strip() +"/9\n"
                grade_string += "Comment : " + lst[11].strip() + "\n\n"
		grade_string += "1.2.6  : " + lst[12].strip() +"/9\n"
                grade_string += "Comment : " + lst[13].strip() + "\n\n"
                grade_string += "1.2.7  : " + lst[14].strip() +"/9\n"
                grade_string += "Comment : " + lst[15].strip() + "\n\n"
		grade_string += "1.2.8  : " + lst[16].strip() +"/10\n"
                grade_string += "Comment : " + lst[17].strip() + "\n\n"
		grade_string += "1.2.9  : " + lst[18].strip() +"/10\n"
                grade_string += "Comment : " + lst[19].strip() + "\n\n"
		grade_string += "1.2.10  : " + lst[20].strip() +"/10\n"
                grade_string += "Comment : " + lst[21].strip() + "\n\n"
		grade_string += "1.2.11  : " + lst[22].strip() +"/10\n"
                grade_string += "Comment : " + lst[23].strip() + "\n\n"
		grade_string += "total   : " + lst[24].strip() +"/100\n"

                #with open(svn_root+"/../sample.txt","a") as p:
                if os.path.exists(path):
                    os.remove(path)
		with open(path,"a") as p:
                    p.write(grade_string)
	        svn_add(path)
