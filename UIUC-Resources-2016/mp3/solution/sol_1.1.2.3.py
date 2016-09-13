from Crypto.Cipher import AES
import struct
import sys

with open(sys.argv[1]) as f:
	cipher = f.read().decode("hex")
iv = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

prefix = "\x00" * 31

for i in range(32):
	key = prefix + struct.pack("B", i)
	aes = AES.new(key, AES.MODE_CBC, iv)

	print str(i) + " " + aes.decrypt(cipher)