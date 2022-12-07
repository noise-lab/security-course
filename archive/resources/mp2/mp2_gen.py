#distribution script for SP16-ECE422

import os
import sys
import hashlib
from shutil import copyfile

def svn_add(path):
    os.system('svn add ' + path)

def generate_files(netid):
    basepath = netid + '/mp2/'

    if not os.path.isdir(basepath):
        os.mkdir(basepath)
        os.mkdir(basepath+"bungle/")
        os.mkdir(basepath+"bungle/views/")
        svn_add(basepath)

    ### Generate Blank Files for solution
    # (filename, initial content)
    empty_files = [('partners.txt',''),
                   ('2.1.2.txt', ''),
                   ('2.2.1.1.txt', ''),
                   ('2.2.1.2.txt', ''),
                   ('2.2.1.3.txt', ''),
                   ('2.2.1.4.txt', ''),
                   ('2.2.2.1.html', ''),
                   ('2.2.2.2.html', ''),
                   ('2.2.3.2_payload.html', ''),
                   ('2.2.3.1.txt', ''),
                   ('2.2.3.2.txt', ''),
                   ('2.2.3.3.txt', ''),
                   ('2.2.3.4.txt', ''),
                   ('2.2.3.5.txt', ''),
                   ('2.2.3.6.txt', '')]
    for empty_file in empty_files:
        (filename, content) = empty_file
        filepath = basepath + filename
        with open(filepath, 'w') as f:
            f.write(content)
        svn_add(filepath)

    """ checkpoint 1 skeleton code """

    bungle_path = '/home/hyunbinl/sp16-ece422/_class/_private/mp2/bungle_dist/'

    bungle_files = ['database.py',
                    'defenses.py',
                    'project2.py',
                    'views/index.tpl',
                    'views/base.tpl',
                    'views/search.tpl']
    
    for bungle_file in bungle_files:
        src = bungle_path+bungle_file
        dst = basepath+"bungle/"+bungle_file
        copyfile(src,dst) 
        svn_add(dst)

    m = hashlib.sha1(netid)
    hashnet = m.hexdigest()
    n = hashlib.sha256(hashnet)
    db_secret = n.hexdigest()    
    with open(basepath+'bungle/dbrw.secret', "w") as f:
        f.write(db_secret)
    svn_add(basepath+'bungle/dbrw.secret')

local_svn_repo = '/home/hyunbinl/sp16-ece422/'
#staff_roster = local_svn_repo + '_rosters/staff.txt'
student_roster = local_svn_repo + '_rosters/students.txt'

os.chdir(local_svn_repo)

#with open(staff_roster) as f:
#    for netid in f:
#        netid = netid.strip()
#        generate_files(netid)

with open(student_roster) as f:
    for netid in f:
        netid = netid.strip()
        generate_files(netid)

#os.system('svn commit -m "Distribute Files for MP2"')
