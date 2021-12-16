import os.path

# prints out netids that appears in partners.txt file more than twice
count_map = {}

#TODO: change this
svn_root = "/home/hyunbinl/sp16-ece422/"
with open(svn_root+"_rosters/students.txt") as f:
	for netid in f:
		netid = netid.strip() 
                if not os.path.exists(svn_root+netid+"/mp2/"):
                    continue
                if not os.path.isfile(svn_root+netid+"/mp2/partners.txt"):
                    continue
		with open(svn_root+netid+"/mp2/partners.txt") as ff:
                        check = 0
			for line in ff:
				if line.strip() == '':
					continue
                                if line.strip() in count_map:
                                    if line.strip() != netid:
					print line.strip()+" found at "+netid
				else:
                                    if line.strip() != netid:
                                        count_map[line.strip()] = 1
                                        check = 1
                        if check == 1:
                            count_map[netid] = 1
