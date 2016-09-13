import sys
import os.path

# find the netid of the partner of argv[1]
student = sys.argv[1]

svn_root = "/home/ubuntu/Desktop/sp16-ece422/"
with open(svn_root+"_rosters/students.txt") as f:
	for netid in f:
		netid = netid.strip()
                if not os.path.exists(svn_root+netid+"/mp1/"):
                    continue
                if not os.path.isfile(svn_root+netid+"/mp1/partners.txt"):
                    continue
		with open(svn_root+netid+"/mp1/partners.txt") as ff:
			for line in ff:
				if line.strip() == student:
					print netid
					#exit(0)

