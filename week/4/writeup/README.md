Writeup 3 - Pentesting I
======

Name: Katam Varsha Reddy
Section: 115069275

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Katam Varsha Reddy

## Assignment 4 Writeup

### Part 1 (45 pts)                                                                                                                       

I first executed "nc cornerstoneairlines.co 45" in the kali linux terminal. When prompted for the IP address I put in 142.93.117.193 and nothing happened. Then i tried executing various low level command line injection commands along with the IP address such as 
142.93.117.193 ls /
142.93.117.193; ls /
Then i tried executing with SHELL ESCAPES such as |, && and ...
When I typed in 142.93.117.193| ls / I was able to view all the directories. Then i was able to navigate into the home directory using ls /home. I checked the home directory first as that was where the flightrecords were. Inside the home directory i found a flag.txt file.
To view its contents I did: 142.93.117.193| cat /home/flag.txt                                                                             
Flag: Good! Here's your flag: CMSC389R-{p1ng_as_a_$erv1c3}

### Part 2 (55 pts)
*Put your writeup >= 200 words here in response to part 2 prompt. Your code for part 2 should be copied into a file in the /writeup directory and pushed there as well*
