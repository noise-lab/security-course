.global your_asm_fn
.section .text

your_asm_fn:

push	%ebp
mov	%esp,%ebp

push	$0
push	$0x646f6f66
push	$0x6c6f6f63
mov	%esp,%ebx
push	$0xc105ed
mov	%esp,%eax
push	%eax

push	%ebx
push	%eax
push	$0xacce55ed

call	practice

leave
ret
