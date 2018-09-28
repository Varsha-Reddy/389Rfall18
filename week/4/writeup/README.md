Writeup 3 - Pentesting I
======

Name: Katam Varsha Reddy
Section: 115069275

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Katam Varsha Reddy

## Assignment 4 Writeup

### Part 1 (45 pts)                                                                                                                       
First i ran nmap on the IP address 142.93.117.193 and found out that port 1337 was closed. 
I executed "nc cornerstoneairlines.co 45" in the kali Linux terminal. When prompted for the IP address I put in 142.93.117.193 and nothing happened. 
Next, tried executing various low-level command line injection commands along with the IP address such as 142.93.117.193; 142.93.117.193 ls /
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
For example, a regular expression such as ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$ will help in validating a users input by making sure
the string contains nothing but an IP address. 

### Part 2 (55 pts)
To make the shell, I used if else statements to first check to check for "shell", "help" and "quit" in the command entered by the user.
I used the raw_input() function which prompts the user to enter their input and returns the data in the form of a string. I kept track of the current (/) and previous directories. Inside a while loop that keeps running as long as the user does not input "exit", I used the socket to connect to cornerstoneairlines with port 45. Inside the shell, I checked for "cd" in the case of a user wanting to navigate through directories. The current and previous directories are updated accordingly. Then I used s.send() to send the new command and print the data. The "help" command prints out the help menu and "quit" exits from the shell. 
