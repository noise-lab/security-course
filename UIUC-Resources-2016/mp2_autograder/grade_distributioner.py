import os
import csv
from datetime import datetime,timedelta;

def svn_add(path):
    os.system('svn add ' + path)

#filename = './mgande2_sep.csv'
filename = './grades/separated_mp2.2_grades.csv'

currtime = datetime.now().strftime("%Y%m%d_%H%M%S")

f = open(filename)
csv_f = csv.reader(f)
gr = open("./grades/grade_mp2.2_late_grade_final_"+str(currtime)+".csv","w",0)

for row in csv_f:
    netid = row[0]
    output = "grade report for "+netid+"\n"

    sql_0 = row[1]
    sql_0c = row[2]
    sql_1 = row[3]
    sql_1c = row[4]
    sql_2 = row[5]
    sql_2c = row[6]
    sql_3 = row[7]
    sql_3c = row[8]
    sql_total = float(sql_0) + float(sql_1) + float(sql_2) + float(sql_3)
 
    output = output + "\n2.2.1 SQL INJECTION\n"
    output = output + "grade for 2.2.1.1: "+sql_0+"/5\n"
    output = output + "comment for 2.2.1.1: "+sql_0c+"\n"
    
    output = output + "grade for 2.2.1.2: "+sql_1+"/5\n"
    output = output + "comment for 2.2.1.2: "+sql_1c+"\n"

    output = output + "grade for 2.2.1.3: "+sql_2+"/10\n"
    output = output + "comment for 2.2.1.3: "+sql_2c+"\n"

    output = output + "grade for 2.2.1.4: "+sql_3+"/10\n"
    output = output + "comment for 2.2.1.4: "+sql_3c+"\n"
    output = output + "TOTAL: "+str(sql_total)+"/30\n"

    csrf_0 = row[9]
    csrf_0c = row[10]
    csrf_1 = row[11]
    csrf_1c = row[12]
    csrf_total = float(csrf_0) + float(csrf_1)

    output = output + "\n2.2.2 CSRF\n"
    output = output + "grade for 2.2.2.1: "+csrf_0+"/10\n"
    output = output + "comment for 2.2.2.1: "+csrf_0c+"\n"
    
    output = output + "grade for 2.2.2.2: "+csrf_1+"/10\n"
    output = output + "comment for 2.2.2.2: "+csrf_1c+"\n"
    output = output + "TOTAL: "+str(csrf_total)+"/20\n"

    xss_0 = row[13]
    xss_0c = row[14]
    xss_payload = row[15]
    xss_payloadc = row[16]
    xss_1 = row[17]
    xss_1c = row[18]
    xss_2 = row[19]
    xss_3 = row[21]
    xss_4 = row[23]
    xss_5 = row[25]
    xss_2c = row[20]
    xss_3c = row[22]
    xss_4c = row[24]
    xss_5c = row[26]

    xss_total = float(xss_0) + float(xss_payload) + float(xss_1) + float(xss_2) + float(xss_3) + float(xss_4) + float(xss_5) 

    output = output + "\n2.2.3 XSS\n"
    output = output + "grade for 2.2.3.1: "+xss_0+"/5\n"
    output = output + "comment for 2.2.3.1: "+xss_0c+"\n"
    output = output + "submission of 2.2.3.2_payload.html: "+xss_payload+"/4\n"
    output = output + "comment for 2.2.3.2_payload.html: "+xss_payloadc+"\n"
    output = output + "grade for 2.2.3.2: "+xss_1+"/21\n"
    output = output + "comment for 2.2.3.2: "+xss_1c+"\n"    
    output = output + "grade for 2.2.3.3: "+xss_2+"/5\n"
    output = output + "comment for 2.2.3.3: "+xss_2c+"\n" 
    output = output + "grade for 2.2.3.4: "+xss_3+"/5\n"
    output = output + "comment for 2.2.3.4: "+xss_3c+"\n" 
    output = output + "grade for 2.2.3.5: "+xss_4+"/5\n"
    output = output + "comment for 2.2.3.5: "+xss_4c+"\n"  
    output = output + "grade for 2.2.3.6: "+xss_5+"/5\n"
    output = output + "comment for 2.2.3.6: "+xss_5c+"\n"

    output = output + "TOTAL: "+str(xss_total)+"/50\n"

    total = sql_total + csrf_total + xss_total    
    output = output + "\nTOTAL: "+str(total)+"/100\n" 

    print output

    path = '/home/hyunbinl/sp16-ece422/'+netid+'/mp2/grade_report_extension_mp2.2_'+str(currtime)+'.txt'
    #TODO: uncomment these
    with open(path,'w') as grade_file:
        grade_file.write(output)
        svn_add(path)
    gr.write(netid+","+str(total)+"\n")
