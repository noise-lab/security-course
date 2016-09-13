#!/usr/bin/python
import os
import time

while(True):
    os.system('networksetup -setairportpower en1 off')
    time.sleep(5)
    os.system('networksetup -setairportpower en1 on')
    time.sleep(1800)
