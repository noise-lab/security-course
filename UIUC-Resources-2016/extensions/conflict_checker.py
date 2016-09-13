#a symple python code for checking conflicts for extensions

import sys

if len(sys.argv) < 2:
    print "usage: python conflict_checker.py [a list of netids]"
    exit()

main_f = open("cs461_mp_extension.txt", "r")
new_f = open(sys.argv[1], "r")

main_buf = main_f.readlines()
new_buf = new_f.readlines()

for netid_old in main_buf:
    for netid_new in new_buf:
        netid_old = netid_old.strip()
        netid_new = netid_new.strip()
        if netid_new == netid_old:
            print "Conflict found! "+netid_new+" already used his/her extension."
