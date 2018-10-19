Writeup 7 - Forensics I
======

Name: Katam Varsha Reddy
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Katam Varsha Reddy

## Assignment 7 writeup

### Part 1 (40 pts)

1. It is a JPEG file (via file image command)

2. Building: John Hancock Center                                                                                                              Street Address: 875 N Michigan Ave, Chicago, IL 60611, USA                                                                      
   (via exiftool image command and gps-coordinates converter)

3. The photo was taken on 22nd August, 2018 at 11:33:24                                                                                        (via exiftool image command)                                                                     

4. iPhone 8                                                                                                                                   (via exiftool image command)

5. 539.5 m Above Sea Level                                                                                                                    (via exiftool image command)

6. I found two flags:                                                                                                                 CMSC389R-{abr@cadabra} (via 'binwalk --dd"png:png" image' command and 'display 248F20.png' command)                                        You found the hidden message! CMSC389R-{look_I_f0und_a_str1ng}  (via 'strings image | grep -C1 "{" ' command)

### Part 2 (55 pts)

*SUBMIT YOUR WRITEUP DETAILING YOUR APPROACH AND SOLUTION TO THIS PROBLEM HERE (>250 words). Dont forget to include the flag!*
