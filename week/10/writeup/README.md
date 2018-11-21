Writeup 10 - Crypto II
=====

Name: Varsha Reddy
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Varsha Reddy

## Assignment 10 Writeup

### Part 1 (70 Pts)
First, I ran the command nc 142.93.118.186 1234 to see how the shell works. Using the information we were given about the length of the secret, I used a 'for' loop to go through all bytes between 6 and 16. The tricky part was to try and understand how to construct payload with appropriate padding. I used the following logic: 
The secret takes up anywhere between 6 to 15 bytes, that is 8 bytes from 7 to 14. 
As we go through the loop, the index size also has to be accounted for. In addition to size, the length of the secret is also calculated.
The Md5 block is 64 bytes long.
This results in 64 - 8 - size - length(message) = 56 - size - len(message)
I looped through the range between 1 and the value calculated above, to add padding. Using the information on https://blog.skullsecurity.org/2012/everything-you-need-to-know-about-hash-length-extension-attacks, I implemented the following:
Padded the string with a '1' bit and some number of '0' bits, followed by the length of the string. In hex, the padding is a 0x80 byte followed by some number of 0x00 bytes and then the length.  
On running stub.py I got the flag: CMSC389R-{i_still_put_the_M_between_the_DV}
![image](https://user-images.githubusercontent.com/42913716/48812447-68de9280-ed00-11e8-88e6-fd5189964211.png)

### Part 2 (30 Pts)
I used the following commands:
1. gpg --import pgpassignment.key to import the given public key. The output included the name of the owner.
![image](https://user-images.githubusercontent.com/42913716/48814321-5405fd00-ed08-11e8-9ce6-487472dc7725.png)
2. gpg -e -u "Varsha Reddy" -r "UMD Cybersecurity Club" message.txt to encrypt a message in message.txt
This created a file called message.txt.gpg.
![image](https://user-images.githubusercontent.com/42913716/48814472-d8588000-ed08-11e8-9ba8-c5681f221966.png)
3. I re-ran the above command gpg -e -u "Varsha Reddy" -r "UMD Cybersecurity Club" message.txt > message.private to dump the output to a file. 
![image](https://user-images.githubusercontent.com/42913716/48814544-23729300-ed09-11e8-8821-d0f9d9c50a46.png)
4. The command to generate keys: gpg --gen-key
