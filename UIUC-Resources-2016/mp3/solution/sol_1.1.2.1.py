import sys

with open(sys.argv[1]) as f:
	text = f.read()

with open(sys.argv[2]) as f:
	key = f.read()

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

out = ''
for c in text:
	if c in key:
		out += s[key.find(c)]
	else:
		out += c

with open(sys.argv[3], 'w') as f:
	f.write(out)
