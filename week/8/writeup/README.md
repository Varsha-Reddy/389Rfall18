Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Katam Varsha Reddy
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Varsha Reddy 

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. The ip address 128.8.120.43 hosts the University of Maryland Cybersecurity Club http://csec.umd.edu/. 
![image](https://user-images.githubusercontent.com/42913716/47868849-b63fa200-dddb-11e8-88bb-355bcb80f3a6.png)

2. The names used by the hackers are c0uchpot4doz and laz0rh4x

3. The IP addresses used by the hackers laz0rh4x and c0uchpot4doz are 142.93.118.186 and 206.189.113.189 respectively. 
   They are connecting from DIGITAL OCEAN INC (101 Ave of the Americas, 10th Floor, New York). I used WHOIS on the ip addresses to get this information
   ![image](https://user-images.githubusercontent.com/42913716/47867798-f6e9ec00-ddd8-11e8-811d-b73e9782ad97.png)

4. Their destination port is 2749 and destination source is 142.93.118.186
   ![image](https://user-images.githubusercontent.com/42913716/47866827-36630900-ddd6-11e8-97b1-daf3e86c4161.png)

5. Yes, they did mention their plans. In their chat, laz0rh4x mentions "we're all set for tomorrow at 1500" (packet 260). The time stamp    of this packet is 24th October, 2018 at 22:42:48.486201. I had to change the time display format under "View" to retrieve this          information. They're planning to meet on 25th October at 15:00 (3:00pm). I used wiresharks follow TCP stream to get this information. 
   ![image](https://user-images.githubusercontent.com/42913716/47866206-7a550e80-ddd4-11e8-949c-c699104de887.png)
   ![image](https://user-images.githubusercontent.com/42913716/47867382-b63da300-ddd7-11e8-8284-e5545b811c56.png)

6. Yes, they did share a google drive link : https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing
   This contains the update.fpff file. 

7.  25th October at 15:00 (3:00pm)

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1. Timestamp: 1540428007. On using a timestamp to human date format it was generated on GMT: Thursday, October 25, 2018 12:40:07 AM
2. The author is laz0rh4x
   ![image](https://user-images.githubusercontent.com/42913716/47883072-147f7b80-de02-11e8-8452-937c28d1f3a3.png)

3. The header says there are 9 sections. But in reality there are 11 sections that are visible in the body

4. ![image](https://user-images.githubusercontent.com/42913716/47883169-73dd8b80-de02-11e8-936f-9c98f114e279.png)
![image](https://user-images.githubusercontent.com/42913716/47883191-89eb4c00-de02-11e8-92f6-9d3c4b17443c.png)

5.
