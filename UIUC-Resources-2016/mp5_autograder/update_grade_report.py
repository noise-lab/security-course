import os
import sys

def svn_delete(path, filename):
    os.system('svn delete --force ' + path + '/mp5/' + filename)

local_svn_repo = '/Users/LittlePrince/Courses/cs461/fall15/svn/fa15-cs461/'
me_only = local_svn_repo + '_rosters/meonly.txt'
staff_roster = local_svn_repo + '_rosters/staff.txt'
student_roster = local_svn_repo + '_rosters/students.txt'

os.chdir(local_svn_repo)

with open(student_roster) as f:
#with open(me_only) as f:
    for netid in f:
        netid = netid.strip()
        svn_delete(netid, "grade_report_20151119_025814.txt")

