import sys

def read_file(filename):
	with open(filename) as f:
		ret = int(f.read(), 16)
	return ret

def write_file(filename, content):
	with open(filename,'w') as f:
		f.write(content)

c = read_file(sys.argv[1])
d = read_file(sys.argv[2])
n = read_file(sys.argv[3])

write_file(sys.argv[4], hex(pow(c,d,n)).replace('L',''))