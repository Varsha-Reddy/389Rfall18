Writeup 3 - Pentesting I
======

Name: Katam Varsha Reddy
Section: 115069275

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Katam Varsha Reddy

## Assignment 4 Writeup

### Part 1 (45 pts)                                                                                                                       

I first executed "nc cornerstoneairlines.co 45" in the kali Linux terminal. When prompted for the IP address I put in 142.93.117.193 and nothing happened. 
Next, tried executing various low-level command line injection commands along with the IP address such as 142.93.117.193 ls /
142.93.117.193; ls /
I also tried executing commands with SHELL ESCAPES such as |, && and ...
When I typed in 142.93.117.193| ls / I was able to view all the directories. I was able to navigate into the home directory using ls /home. 
I checked the home directory first as that was where the flight records were for the previous write-ups. Inside the home directory, I found the flag.txt file. To view its contents I ran: 142.93.117.193| cat /home/flag.txt                                                                             
Flag: Good! Here's your flag: CMSC389R-{p1ng_as_a_$erv1c3}
To find all the script files I ran: find . -type f -executable. 
I found a large number of files. I navigated to the first executable file containter_startup.sh 
by running the command cat ./opt/container_startup.sh 
Based on the contents of this file, Fred is not validating his input. Fred could prevent this vulnerability by validating commands against a whitelist of allowed IPs.
In regards to arguments, he could whitelist regular expressions and ensure characters such as | && ; are not a part of the expression. Anything other than a valid IP
should be rejected and all other characters, commands should be validated.
He could also use regular expressions that only allow numbers and dots. 
For example, ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$ will help in validating a users input by making sure
the string contains nothing but an IP address. 

### Part 2 (55 pts)
*Put your writeup >= 200 words here in response to part 2 prompt. Your code for part 2 should be copied into a file in the /writeup directory and pushed there as well*
