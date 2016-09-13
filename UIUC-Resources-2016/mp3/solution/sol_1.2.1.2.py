from pymd5 import md5, padding
from urllib import quote
import sys

def read_file(filename):
	with open(filename) as f:
		ret = f.read()
	return ret

def write_file(filename, content):
	with open(filename,'w') as f:
		f.write(content)

orig = read_file(sys.argv[1])
cmd = read_file(sys.argv[2])

q = orig.split('&')
token = q[0][q[0].find('=')+1:]

h = md5(state=token.decode('hex'), count=512)
h.update(cmd)
tokenval = h.hexdigest()
newcmd = "token="+tokenval+orig[orig.find('&'):]+quote(padding((len(orig[orig.find('&')+1:])+8)*8))+cmd

write_file(sys.argv[3], newcmd)