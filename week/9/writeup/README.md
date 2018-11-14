Writeup 9 - Crypto I
=====

Name: Katam Varsha Reddy
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Varsha Reddy

## Assignment 9 Writeup

### Part 1 (60 Pts)
I iterated through the hashlist, wordlist and salts using for loops. I appended salt and the password from the wordlist with the help of hashlib.sha512(). I used the rstrip() function to get rid of any trialing characters in "word". Next, I used the hash.hexdigest() function that returns the digest as a string obj of double length of the data passed to the update() method. If the password is found in the wordlist, the password and salt are displayed. The following are the results produced when part1.py is executed.

![image](https://user-images.githubusercontent.com/42913716/48454858-fc571700-e786-11e8-8b23-2b5cc376e479.png)

### Part 2 (40 Pts)
Using the given information: nc 142.93.117.193 7331, I filled in the IP address and port in part2.py and executed it to see what the results would be. I observed that the output said: "Hello there! Welcome to my hash workshop" along with a statement that specified which secure hash algorithm is to be used to hash a given string. In order to get the SHA type and the string, I used regular expressions by importing re. Initially, I tried to use an else-if block to check for each possible type of SHA in the given string, but using regular expressions made it more compact and easy. Using re.findall() I got the SHA type and string via value[0][0] and value[0][1]. The loop continues until it finds a statement that does not say "Find me the". Below are the results of "python part2.py"
Flag found: CMSC389R-{H4sh-5l!ngInG-h@sH3r}
![image](https://user-images.githubusercontent.com/42913716/48455400-fb26e980-e788-11e8-9453-718a6d7665c5.png)
![image](https://user-images.githubusercontent.com/42913716/48455403-ffeb9d80-e788-11e8-9ecf-2719bbabbf75.png)



