#python file which separates teams so that individuals can get grades

out = {}
sss = []

#TODO: change path when grading
with open('mgande2.csv') as f:
	for line in f:
		line = line.strip()
		netids = line[:line.find(',')].split('-')
		if netids[0] == '': #empty submission
			continue
		for netid in netids:
			sss.append(netid+line[line.find(','):])
			if netid in out:
				old = out[netid]
				new = line[line.find(','):]

				s_old = old[old.rfind(',')+1:]
				s_new = new[new.rfind(',')+1:]

				if s_new > s_old:
					out[netid] = new

			else:	
				out[netid] = line[line.find(','):]

arr = []
for elem in out:
	arr.append(elem+out[elem])

arr.sort()
for elem in arr:
	print elem

# sss.sort()
# print 'sss'
# for elem in sss:
# 	print elem
