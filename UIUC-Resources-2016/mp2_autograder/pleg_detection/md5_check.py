#prints a list of netids which uses password from cvk's blog as solution for 2.2.1.3

import os
import urllib

def md5_check(netid):
    basepath = netid + '/mp2/'
    filename = '2.2.1.3.txt'
    filepath = basepath + filename
    password = get_password(filepath)
    if password == '129581926211651571912466741651878684928':
        print netid    


def get_password(path):
    text = extract(path)
    index = text.find('password=')
    encoded_password = text[index + 9:]
    try:
        return urllib.unquote(encoded_password).decode('utf8')
    except:
        return ""

def extract(path):
    try:
        with open(path) as f:
            return f.read().strip()
    except:
        return ""

#TODO: change this
local_svn_repo = '/home/hyunbinl/cs461/sp16-ece422/'
student_roster = local_svn_repo + '_rosters/students.txt'

os.chdir(local_svn_repo)

with open(student_roster) as f:
    for netid in f:
        netid = netid.strip()
        md5_check(netid)
