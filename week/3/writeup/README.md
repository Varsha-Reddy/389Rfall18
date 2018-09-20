Writeup 3 - OSINT II, OpSec and RE
======

Name: KATAM VARSHA REDDY
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Varsha Reddy

## Assignment 3 Writeup

### Part 1 (100 pts)
1. Weak Passwords
Fred Kruger's username is kruegster and password is pokemon. His password was extremely easy to guess given his liking for pokemon that he conveyed through Instagram and a Twitter. I was able to guess his password and username and gain access to the server prior to running code that went through the "rockyou" wordlist. This indicates that the password is weak and very common. According to an article by Paul Rubens, a password made up of six lower case letters can be guessed by a computer in a fraction of a second. However, A password made up of 11 lower and upper case letters, special characters and numbers takes up to 500 years. I would suggest Fred to not use personal information or interests as a password. A hacker who can gather ample information about an individual can easily guess their password. Fred can use a password manager such as dashlane to securely store passwords and personal information. It sends out real-time alerts. Dashlane also helps in generating strong passwords that can help in resisting hacks. It generates strong passwords by using a secure technology with built-in randomness. Having the same strong password for all accounts negates the advantages of having one. Dashlane can help in remembering and storing passwords for multiple accounts. 

Sources: https://www.dashlane.com/features/password-generator
https://www.dashlane.com/
https://www.techradar.com/news/internet/policies-protocols/10-ways-to-make-your-passwords-secure-1155444

2. Open Ports
Port 1337 was open. Anyone with an IP address, username and password can access the administrator portal through the port. Open ports expose services, that are listening on those ports, to exploits. Through nmap, I found out that port 22 was open with ssh service, and port 80 was open with HTML service. I would suggest Fred to not leave port 1337 open. Instead, he could use port 22 with a private key. This will ensure controlled connections and access. Through SSH keys, only an authorized person can gain access to the server. This adds an extra layer of security. Since private keys never get sent over the network, there is no possibility for a man-in-the-middle attack. Fred could also use a firewall such as pfSense. This will ensure there is a limitation to port connection and help in reducing the areas exposed. pfSense is an open source security solution with features such as IP/port filtering, limiting connections, layer 2 capable, and scrubbing. 

Sources: https://blog.vpscheap.net/the-importance-of-ssh-keys-and-how-to-create-them/
https://geekflare.com/best-open-source-firewall/
https://www.pfsense.org/

3. Hidden Directories and robots.txt 
Using robots.txt to protect or hide any information can be a security risk. Fred has a hidden directory called secret that shows up when a user navigates robots.txt. Since robots.txt is publicly accessible, any hidden directories or files on the server will be exposed. Fred should use robots.txt for what it is intended to do, that is, suggest robots how to crawl pages on his website. He should consider using other security methods such as firewalls and password protecting. He shouldn't be using robots.txt for hidden directories. Instead, he should move sensitive files and the "secret" directory into a subdirectory and exclude that subdirectory by itself. 

Sources: http://www.chami.com/tips/internet/040498I.html





