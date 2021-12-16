import sys

# sum the grade on each line then takes the highest grade of each student
filepath = "/home/ubuntu/Desktop/grade.txt"

scores = {}

with open(filepath) as f:
	for line in f:
		lst = line.strip().split(',')
		total = 0
		netid = lst[0]
		for i in range (6):
			total += int(lst[2*i+2])
		line =  line.strip() + ", "+str(total)

		if netid in scores:
			print netid
			if total > scores[netid][2]:
				scores[netid] = (netid+','+str(total),line,total)
		else:
			scores[netid] = (netid+','+str(total),line,total)
tlst = []
llst = []
for key in scores:
        tlst.append(scores[key][0])
	llst.append(scores[key][1])

for elem in tlst:
        with open("/home/ubuntu/Desktop/cp1_grades.csv","a") as f:
            f.write(elem+"\n")

llst.sort()
for elem in llst:
	print elem
        with open("/home/ubuntu/Desktop/cp1_processed_grades.txt","a") as f:
            f.write(elem+"\n")
