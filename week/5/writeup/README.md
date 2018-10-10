Writeup 5 - Binaries I
======

Name: Katam Varsha Reddy
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Katam Varsha Reddy

## Assignment 5 Writeup
I started off by drawing a diagram to understand how base pointers, return addresses and variables are stored. This helped me understand how the base pointer keeps track of functions and how new frames are created. Next, I started coding and figured out the str pointer was stored in rdi which is used to pass 1st argument, rsi for the second argument val, and rcx as a counter to keep track of string length. I created a loop that checks for the condition, i < len. If true, the value gets added to array, otherwise control jumped to a branch that exited out.
When I first ran the code, i encountered a segmentation fault. I tried to debug it using gdb and by adding break points. I figured the seg fault might have been due to the stack not having the right return value after jumping to the end. I also realised that I wasn't increamenting the value of 'i' properly.
Upon fixing those issues, my code was compiling and i was able to run ./main
It displayed Hello zzzzzz instead of Hello zzzzz!, I assumed this was due one of the three reasons: 
1. buffer overflow 
2. I was moving with 'qword' instead of moving a single byte at a time. 
3. The loop was running one extra time
To fix it, I changed my loop which was previously 'jl' to 'jle'. Next, I had to figure out how to move bytes instead of words. So I changed my previous mov statement from mov[rdi + rcx], rsi to mov [rdi +rcx], sil
This helped me copy a single character at a time like how C does. 
For the second function, I followed the same exact method I used for the first functin by using a loop that checks if i < len and assigns dest[i] = scr[i]. I used mov al, [rsi+rcx] and mov [rdi+rcx], al.
