global _start
extern scanf		
extern printf

section .bss
var: resd 1

section .text
_start:
	mov rdi, format		
	mov rsi, var		
	mov rax, 0			
	call scanf
	
	mov eax, [var]
	xor rbx, rbx
	mov bx, ax
	mov [var], ebx
	
	
	mov rdi, format		
	mov rsi, [var]		
	mov rax, 0
	call printf
	
	xor rax, rax
	ret

format: db "%d", 10, 0
