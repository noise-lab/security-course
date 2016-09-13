.global your_asm_fn
.section .text

your_asm_fn:

push	%ebp
mov	%esp,%ebp

push	$0xffffffff
pop	%eax


call	output


leave
ret
