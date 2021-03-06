section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

	mov rcx, 0

func1: cmp rdx, rcx
       jle exit     
      mov [rdi+rcx], sil
      add rcx, 1
      ;sub rdx, rbx
      jmp func1
exit:

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov rcx, 0
     
func2: cmp rdx, rcx
       jle exit
       mov al, [rsi + rcx]
       mov [rdi + rcx], al
       add rcx, 1
       jmp func2
