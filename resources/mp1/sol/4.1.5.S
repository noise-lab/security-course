.global _main
.section .text

_main:

push	%ebp
mov	%esp,%ebp

mov	$11,%eax
xor	%edx,%edx
push	$0
push	$0x0068732f
push	$0x6e69622f
mov	%esp,%ebx
push	$0
push	%ebx
mov	%esp,%ecx
int	$0x80

leave
ret
