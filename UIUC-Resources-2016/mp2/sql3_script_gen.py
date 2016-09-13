#this is a python code which creates SQL script for 2.2.1.4 database

import hashlib

f1 = open('netid.txt', 'r')

secret = ['alpha',
'brabo',
'charlie',
'delta',
'echo',
'foxtrot',
'golf',
'hotel',
'india',
'juliett']

for l in f1:
    netid = l.strip()
    md5 = hashlib.md5(netid).hexdigest()
    
    output = 'insert into SECRET (hash,secret) values (\'' + md5 + '\', \'' + secret[int(md5,16)%10] + '\');'
    print output
