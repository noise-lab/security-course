from Crypto.Hash import SHA256
from bitstring import BitArray
import sys

argv = sys.argv

def read_file(filename):
	with open(filename) as f:
		ret = f.read()
	return ret

def write_file(filename, content):
	with open(filename,'w') as f:
		f.write(content)

h = SHA256.new()
h.update(read_file(argv[1]))
x = int(h.hexdigest(),16)

h = SHA256.new()
h.update(read_file(argv[2]))
y = int(h.hexdigest(),16)

diff = bin(x^y)

count = 0
for i in diff:
	if i == '1':
		count+=1;

write_file(sys.argv[3],hex(count))