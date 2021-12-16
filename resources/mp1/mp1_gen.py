import os
import sys

def svn_add(path):
    os.system('svn add ' + path)

def generate_files(netid):
    basepath = netid + '/mp1/'
    if not os.path.isdir(basepath):
        os.mkdir(basepath)
    svn_add(basepath)

    ### Generate Blank Files for solution
    # (filename, initial content)
    empty_files = [('1.1.1_addr.txt', ''),
                   ('1.1.1_eax.txt', ''),
                   ('1.1.2.S', '.global your_asm_fn\n.section .text\n\nyour_asm_fn:\n\npush\t%ebp\nmov\t%esp,%ebp\n\n\nleave\nret'),
                   ('1.1.3.S', '.global your_asm_fn\n.section .text\n\nyour_asm_fn:\n\npush\t%ebp\nmov\t%esp,%ebp\n\n\nleave\nret'),
                   ('1.1.4.S', '.global your_asm_fn\n.section .text\n\nyour_asm_fn:\n\npush\t%ebp\nmov\t%esp,%ebp\n\n\nleave\nret'),
                   ('1.1.5.S', '.global _main\n.section .text\n\n_main:\n\npush\t%ebp\nmov\t%esp,%ebp\n\n\nleave\nret'),
                   ('1.2.1.py', ''),
                   ('1.2.2.py', ''),
                   ('1.2.3.py', ''),
                   ('1.2.4.py', ''),
                   ('1.2.5.py', ''),
                   ('1.2.6.py', ''),
                   ('1.2.7.py', ''),
                   ('1.2.8.py', ''),
                   ('1.2.9.py', ''),
                   ('1.2.10.py', ''),
                   ('1.2.11.py', ''),
                   ('partners.txt', ''),
                   ('cookie', '')
                   ]
    for empty_file in empty_files:
        (filename, content) = empty_file
        filepath = basepath + filename
        with open(filepath, 'w') as f:
            f.write(content)
        svn_add(filepath)




local_svn_repo = '/home/ubuntu/Desktop/sp16-ece422/'
staff_roster = local_svn_repo + '_rosters/staff.txt'
student_roster = local_svn_repo + '_rosters/students.txt'
me = local_svn_repo + '_rosters/me.txt'

os.chdir(local_svn_repo)

with open(me) as f:
    for netid in f:
        netid = netid.strip()
        generate_files(netid)
#os.system('svn ci -m "test"')
#os.system('svn commit -m "Distribute Files for MP1"')
