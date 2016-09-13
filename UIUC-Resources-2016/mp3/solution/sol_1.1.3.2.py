from array import array
import sys

def read_file(filename):
	with open(filename) as f:
		ret = f.read()
	return ret

def write_file(filename, content):
	with open(filename,'w') as f:
		f.write(content)

def wha(str):
	bytes = array("B", str)
	mask = 0x3FFFFFFF
	outHash = 0
	for byte in bytes:
		intermediate_value = ((byte ^ 0xCC) << 24) | ((byte ^ 0x33) << 16) | ((byte ^ 0xAA) << 8) | (byte ^ 0x55)
		outHash =(outHash & mask) + (intermediate_value & mask)
	return outHash

write_file(sys.argv[2],hex(wha(read_file(sys.argv[1]))))