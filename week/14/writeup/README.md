Writeup 10 - Crypto II
=====

Name: Katam Varsha Reddy
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Katam Varsha Reddy

## Assignment 10 Writeup

### Part 1 (70 Pts)
Looking at "Such a quick, little" from the project description, it was clear that SQL injection had to be performed. After analysing the links on the website in the "item table" I noticied that item?id=number changed each item, where number 0,1,or 2. With the help of the example in Week 11 Web slides which used *admin' OR '1'='1'-- -*, I used *'0 or true -- "*. This displayed all the items as well as a
flag.                                                                                                                                   

![image](https://user-images.githubusercontent.com/42913716/49681302-8b490d80-fa6d-11e8-84f3-ec11c52f26b1.png)
![image](https://user-images.githubusercontent.com/42913716/49681279-f34b2400-fa6c-11e8-934e-d725f88b23cc.png)

### Part 2 (30 Pts)
**LEVEL 1**: For this level, the mission was to inject a script to pop up a JavaScript alert() in the frame. I used simple JavaScript, quoted string in a script block. I entered the following query in the search box, *<script>alert("Level 1")</script>*. It prompted me to the next level.

**LEVEL 2**: For this level, I used one of the hints which said that the template does not escape the contents of the status message. On researching a little bit about this, I figured out I had to use an image tag. This was a form of stored XSS attack. I injected the following script in the comment/status box, *<img src=x onerror=alert('Level2')>* and it worked. 
![image](https://user-images.githubusercontent.com/42913716/49679493-d2c59e80-fa59-11e8-99f4-835e0267adb5.png)

**LEVEL 3**: For this level, I had to edit the address in the URL bar. With the help of a hint that suggested that data in the window.location object can be influenced by an attacker, I tried to analyze the target code. I noticed that window.location.hash was set 
'num' which was appended to img src. After several failed attempts, I realised something was wrong with the URL in the game. I switched browsers from Chrome to Explorer. I tried escaping the URL with *'onerror="alert('Level3');"*, and it worked. (No idea why the exact same thing did not work on Chrome)
![image](https://user-images.githubusercontent.com/42913716/49680434-305de900-fa62-11e8-81c3-abfef89e3e2c.png)
![image](https://user-images.githubusercontent.com/42913716/49680628-acf1c700-fa64-11e8-9db0-8addfc02bdd6.png)

**LEVEL 4**: I first clicked on create timer, I noticed that this changes the URL and counts down to the numbers of seconds in the box. This problem looked similar to the one on the previous level. Intially, I tried to use onload=alert("trial")>. When I created the timer, the timer did not stop. The third hint suggested to try entering a single quote (') and watch the error console. When I looked at the error console, I got a better understanding of how the input injection was taking place. I tried inputting *);alert('level4* in the timer box, and it worked.
![image](https://user-images.githubusercontent.com/42913716/49680888-c0eaf800-fa67-11e8-8638-d495827de065.png)

**LEVEL 5**: For this level, I first clicked on "Sign up". I noticed the URL had next=confirm. I looked at the target code of the sign up frame. This gave me some information about how the URL parameter is used. After trying to append tags, I tried to use the third hint which indicated that "javascript" was to be used. I did a little reading on "If you want to make clicking a link execute Javascript (without using the onclick handler), how can you do it?". One useful link was: *https://stackoverflow.com/questions/1265887/call-javascript-function-on-hyperlink-click*. I tried to use *next=javascript:alert("level5")* and I was prompted to the next level.
![image](https://user-images.githubusercontent.com/42913716/49681438-a9b00880-fa6f-11e8-9979-0e6b9539b46e.png)

**LEVEL 6**: For this level, initially I tried to follow the approach by hosting a js file. I tried to create a js file, save it and host it locally. Half way through, I wanted to try a different (easier) method. I noticed that *data:text/javascript* could create an external file. I added an alert call to it and did, *#data:text/javascript,alert('level6')*. 
![image](https://user-images.githubusercontent.com/42913716/49681685-188f6080-fa74-11e8-9129-e5f2d582bfd4.png)
![image](https://user-images.githubusercontent.com/42913716/49681719-83d93280-fa74-11e8-994d-6192f4beb905.png)
