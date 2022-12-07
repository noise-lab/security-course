from hashlib import md5
from string import whitespace
from datetime import datetime
import os
import sys

'''
Note: Every student's svn directory should be updated to the revision just before
      the duedate before this script is run

'''

def svn_checkout(date_str, file):
	'''
	checkout the latest version of the file before the given timestamp

	date_str should be in the format %Y-%m-%d %H:%M
	'''
	svn_cmd="svn up -r {\""+date_str+"\"} --accept mine-conflict "+file
	os.system(svn_cmd);

# for grading
def read_student_solution(filepath):
    with open (filepath, "r") as myfile:
        data = ""
        for line in myfile:
            line = line.strip()
            if not line:
                continue
            if line[0] == "#":
                continue;
            data = data+line

        # remove whitespace    
        data = data.translate(None, whitespace)

    return data

def get_score_string(partners, score):
	ret = ''
	for partner in partners:
		ret += partner.strip() + ',' + str(score) + '\n'

	return ret

def main():
	svn_basedir = sys.argv[1]
	netid_list_path = sys.argv[2]

	curr_time = datetime.now().strftime("%Y%m%d_%H%M%S")

	partner_file_path = svn_basedir + "/{0}/mp3/partners.txt"
	md5_file_path = svn_basedir + "/{0}/mp3/sol_3.2.4_hash.hex"
	ps_file_path = svn_basedir + "/{0}/mp3/sol_3.2.4.ps"

	# instructor grade report file
	gr=open("part_3.2.4_grades_"+str(curr_time)+".txt","w",0);

	# read student list into a list
	with open(netid_list_path, 'r') as f:
		netid_list = f.readlines()

	# grade students
	for netid in netid_list:
		netid = netid.strip()

		# manage partner
		partners = [netid]
		try:
			with open(partner_file_path.format(netid)) as f:
				content = f.readlines()
				if content == []:
					# empty partners.txt, skip
					continue
				else:
					partners = content
		except:
			print 'Malformed partners.txt for {}\n'.format(netid)

		print '\nGrading ' + str(partners)

		# update the hash file
		svn_checkout('2016-03-30 14:02', md5_file_path.format(netid))

		# read the hash 
		submitted_hash = read_student_solution(md5_file_path.format(netid))

		# if hash is not submitted, then done
		if submitted_hash == '' :
			grade = get_score_string(partners, 0)
			print 'Hash file is empty\n'

		else :
			# compute hash of ps file
			with open(ps_file_path.format(netid), 'rb') as hashfile:
				content = hashfile.read()

			ps_file_hash = md5(content).hexdigest()

			# if the hash of the file and the submitted hash is not equal, then done
			if int(ps_file_hash,16) != int(submitted_hash,16):
				grade = get_score_string(partners, 0)
				print 'Hash does not match:\n{}\n{}\n'.format(ps_file_hash,submitted_hash)

			else:
				# check the file content
				os.system('gs '+ps_file_path.format(netid))
				score = input('\nEnter score: ')
				grade = get_score_string(partners, score)

		gr.write(grade)


if __name__ == "__main__":
    main()
