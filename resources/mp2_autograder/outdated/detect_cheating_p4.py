#!/usr/bin/env python

import grade_p4
import shutil
import os
import sys
from grade_p4 import proj_dir

target = sys.argv[1]

with open('cheating_'+target+'.txt', 'w') as cheat_fd:
    cheat_fd.write('Running ' + target + ' project with everyone\'s cookie\n')
    t_cookie_path = os.path.join(proj_dir, target, 'cookie')
    for p in os.listdir(proj_dir):
        cookie = os.path.join(proj_dir, p, 'cookie')
        
        # Skip over target directory
        if cookie != t_cookie_path:
            shutil.copy(cookie, t_cookie_path)
        else:
            continue

        with open(cookie) as f:
            cookie_value = f.read()
            
        score = sum(grade_p4.process(target, False)[1:])
        cheat_fd.write(p + " Cookie: " + cookie_value + " Score: " + str(score) + '\n')
        print p, "Cookie:", str(cookie_value), "Score:", score
        

# reset target cookie
grade_p4.set_cookie(target)
