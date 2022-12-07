#!/usr/bin/python
import os

while True:
    try:
        print "(re)starting..."
        os.chdir('../website')
        os.system('coffee app.coffee')
    except:
        print 'error!'
print 'out of the loop'

