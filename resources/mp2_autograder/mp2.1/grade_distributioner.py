import os
import csv
from datetime import datetime,timedelta;

def svn_add(path):
    os.system('svn add ' + path)

filename = './grades/separated_mp2.1_grades.csv'

currtime = datetime.now().strftime("%Y%m%d_%H%M%S")

f = open(filename)
csv_f = csv.reader(f)
gr = open("./grades/mp2.1_regrade_"+str(currtime)+".csv","w",0)

for row in csv_f:
    netid = row[0]
    output = "grade report for "+netid+"\n"
    
    p1 = row[1]
    p1_c = row[2]
    p2 = str(float(row[3]) + float(row[5]) + float(row[7]) + 
            float(row[9]))
    p2_c = row[4]+' '+row[6]+' '+row[8]+' '+row[10]
    p3 = row[11]
    p3_c = row[12]
    p4 = str(float(row[13]) + float(row[15]))
    p4_c = row[14]+' '+row[16]
 
    output = output + "\n2.1.2 SQL\n"
    output = output + "grade for 2.1.2: "+p1+"/5\n"
    output = output + "comment for 2.1.2: "+p1_c+"\n"
 
    output = output + "\n2.1.3 Prepared Statements\n"
    output = output + "grade for 2.1.3: "+p2+"/5\n"
    output = output + "comment for 2.1.3: "+p2_c+"\n"

    output = output + "\n2.1.4 Input Sanitization\n"
    output = output + "grade for 2.1.4: "+p3+"/5\n"
    output = output + "comment for 2.1.4: "+p3_c+"\n"

    output = output + "\n2.1.5 Token Validation\n"
    output = output + "grade for 2.1.5: "+p4+"/5\n"
    output = output + "comment for 2.1.5: "+p4_c+"\n"

    total = float(p1) + float(p2) + float(p3) + float(p4)
    output = output + "TOTAL: "+str(total)+"/20\n"

    print output

    path = '/home/hyunbinl/sp16-ece422/'+netid+'/mp2/grade_report_mp2.1_'+str(currtime)+'.txt'
    #TODO: uncomment these
    with open(path,'w') as grade_file:
        grade_file.write(output)
        svn_add(path)
    gr.write(netid+","+str(total)+"\n")
