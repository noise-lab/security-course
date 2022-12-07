import os
import sys
import mp5_tools

def svn_add(path):
    os.system('svn add ' + path)

def svn_delete(path, filename):
    os.system('svn delete --force ' + path + filename)

def generate_files(netid):
    basepath = netid + '/mp5/'
    if not os.path.isdir(basepath):
        os.mkdir(basepath)
    svn_add(basepath)

	### Create Directory for evidence files
    solpath = basepath + 'evidence/'
    if not os.path.isdir(solpath):
        os.mkdir(solpath)
    svn_add(solpath)

	### Create Directory for explanation files
    solpath = basepath + 'explanation/'
    if not os.path.isdir(solpath):
        os.mkdir(solpath)
    svn_add(solpath)

    ### Generate Blank Files for solution
    # (filename, initial content)
    empty_files = [('partners.txt', ''),
    			   ('5.1.1.txt', '###Solution Example: ###\n#yann'),
    			   ('5.1.2.txt', '###Solution Example: ###\n#EST'),
    			   ('5.1.3.txt', '###Solution Example: ###\n#bob\n#eve\n#eve'),
    			   ('5.1.4_name.txt', '###Solution Example: ###\n#evidencefile.txt'),
    			   ('5.1.4_time.txt', '###Solution Example: ###\n#04032330'),
    			   ('5.1.5_time.txt', '###Solution Example: ###\n#04032330'),
    			   ('5.1.5_attackerip.txt', '###Solution Example: ###\n#1.2.3.4\n#5.6.7.8'),
    			   ('5.1.5_victimip.txt', '###Solution Example: ###\n#9.10.11.12'),
    			   ('5.2.1_default.txt', '###Solution Example: ###\n#OS X\n#10.10.4'),
    			   ('5.2.1_behavior.txt', '###Solution Example: ###\n#scriptfile.ext'),
    			   ('5.2.1_primary.txt', '###Solution Example: ###\n#OS X\n#10.10.4'),
    			   ('5.2.2.1.txt', '###Solution Example: ###\n#yann'),
    			   ('5.2.2.2_usernames.txt', '###Solution Example: ###\n#bob\n#eve\n#eve'),
    			   ('5.2.2.2_relationship.txt', '###Solution Example: ###\n#k'),
    			   ('5.2.2.3_link.txt', '###Solution Example: ###\n#https://www.google.com/maps\n#https://www.cnet.com/news/'),
    			   ('5.2.2.3_weapon.txt', '###Solution Example: ###\n#lightsaber'),
    			   ('5.2.2.4.txt', '###Solution Example: ###\n#p4ssw0rd'),
    			   ('5.2.2.5_account.txt', '###Solution Example: ###\n#yann'),
    			   ('5.2.2.5_tools.txt', '###Solution Example: ###\n#zip\n#john'),
    			   ('5.2.2.5_ip.txt', '###Solution Example: ###\n#1.2.3.4'),
    			   ('5.2.2.5_connection.txt', '###Solution Example: ###\n#no\n#private_key_file_name\n#public_key_file_name'),
    			   ('5.2.2.5_password.txt', '###Solution Example: ###\n#p4ssw0rd'),
    			   ('5.2.2.6.txt', '###Solution Example: ###\n#filename.ext'),
    			   ('5.2.2.7_accomplice.txt', '###Solution Template: ###\n#contact info'),
    			   ('5.2.2.7_location.txt', '###Solution Example: ###\n#1.234\n#5.678'),
    			   ('5.2.2.7_originaltime.txt', '###Solution Example: ###\n#2330'),
    			   ('5.2.2.7_actualtime.txt', '###Solution Example: ###\n#2330'),
    			   ('5.2.2.8.txt', '###Solution Example: ###\n#Yann Simpson'),
    			   ('5.2.2.9.txt', '###Solution Example: ###\n#yes')]
    
    for empty_file in empty_files:
        (filename, content) = empty_file
        filepath = basepath + filename
        with open(filepath, 'w') as f:
            f.write(content)
        svn_add(filepath)

def generate_files_checkpoint2(netid):
    basepath = netid + '/mp5/'
    vm_path = basepath + 'suspect_vm.txt'
    vm_link = mp5_tools.assign_vm_link(netid)
    with open(vm_path, 'w') as f:
   	    f.write(vm_link)
    svn_add(vm_path)

    code_path = basepath + 'code.txt'
    location_code = mp5_tools.assign_location_code(netid)
    with open(code_path, 'w') as f:
        f.write(location_code)
    svn_add(code_path)

def check_checkpoint2_distribution(netid, path):
    vm_link = mp5_tools.assign_vm_link(netid)
    location_code = mp5_tools.assign_location_code(netid)
    with open(path, 'a+') as f:
        f.write(netid + ',' + vm_link + ',' + location_code + '\n')


local_svn_repo = '/home/lkhwang/Courses/cs461/sp16-ece422/'
me_only = local_svn_repo + '_rosters/meonly.txt'
staff_roster = local_svn_repo + '_rosters/staff.txt'
student_roster = local_svn_repo + '_rosters/students.txt'

os.chdir(local_svn_repo)

# with open(student_roster) as f:
#     for netid in f:
#         netid = netid.strip()
#         my_path = local_svn_repo + '_class/_private/mp5/mp5_checkpoint2.csv'
#         check_checkpoint2_distribution(netid, my_path)

# with open(me_only) as f:
with open(student_roster) as f:
    for netid in f:
        netid = netid.strip()
        generate_files(netid)
        generate_files_checkpoint2(netid)

#os.system('svn commit -m "Distribute Files for MP1"')
