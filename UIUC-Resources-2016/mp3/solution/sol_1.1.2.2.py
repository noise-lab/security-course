from Crypto.Cipher import AES
import struct
import sys

with open(sys.argv[1]) as f:
	cipher = f.read().decode("hex")

with open(sys.argv[2]) as f:
	key = f.read().decode("hex")

with open(sys.argv[3]) as f:
	iv = f.read().decode("hex")

with open(sys.argv[4], 'w') as f:
	f.write(str(AES.new(key, AES.MODE_CBC, iv).decrypt(cipher)))
