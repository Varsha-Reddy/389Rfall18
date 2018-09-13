OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Thursday, September 13 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `kruegster1990`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `kruegster1990` and answer the following questions:

1. What is `kruegster1990`'s real name?
Fred Krueger

2. List all personal information (including social media accounts) you can find about him. For each, briefly detail how you discovered them.
Fred Krueger is from Silver Spring, MD. He was born in 1990. He is the owner of Cornerstone Airlines. He first created his twitter account on 12th August, 2018 at 22:28:06. He has one follower, UMD Cybersecurity and is following the account back. He had a bad experience with Malaysian Airlines on August 18th, 2018.
I found all of the above information through his twitter acccount: https://twitter.com/kruegster1990/
He uses an secure encrpyted mailbox, Tutanota. His mail is: kruegster@tutanota.com
I found this through his companies website : http://www.cornerstoneairlines.co/about.html
He posted an article on Pokemon GO cyber risks on Twitter: https://www2.idexpertscorp.com/knowledge-center/single/can-we-stop-the-pokemon-go-cyber-risks

3. What is the IP address of the webserver hosting his company's site? How did you discover this?
http://142.93.117.193/
I discovered it when i clicked on the "Admin" tab on his company's website. 

4. List any hidden files or directories you found on this website. Did you find any flags?
Yes, I found a hidden directory. I navigated to http://cornerstoneairlines.co/robots.txt 
This gave me a hint to the name of the directory by displaying:
User-agent: *
Disallow: /secret
http://cornerstoneairlines.co/secret/

5. Did you find any other IP addresses associated with this website? What do they link to, or where did you find them?
No, I did not find any other IP addresses

6. If you found any associated server(s), where are they located? How did you discover this?
Apache/2.4.18
Found it by entering a random non-existent URL

7. Which operating system is running on the associated server(s)? How did you discover this?
Apache/2.4.18 (Ubuntu) Server at cornerstoneairlines.co Port 80
I put in a random directory to see if the "Not Found" page would display any information. 

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)

### Part 2

Use the provided python stub code [('stub.py')](stub.py) or write your own program in another language to gain access to the Cornerstone Airlines administrator server via an open port that you should have found in Part 1. 

Once you have gained access to the Cornerstone Airlines administrator portal with the correct login credentials, you will have access to a system shell. 

Use your knowledge of Linux and OSINT techniques to locate a specific flight record, read it, and submit the flag inside.

Your response here should briefly document how you approached and solved this part of the assignment. You should also push your bruteforce program to the "week/2/writeup" folder of your GitHub repository.

Note: If you choose to write your own program in another language, please include instructions on how to execute your program, including what version of the language you are using. You will **NOT** receive credit if the TAs cannot run your program.

If you are stuck on this part of the assignment, let us know! The facilitator staff is here to help and teach, and we are open to releasing hints as time goes on!

### Format
In the "week/2/writeup" directory of our repository there is a README.md file for you to edit and submit your homework in. Use this as a template and directly edit it with your answers. Complete your bruteforce program in this directory as well. When you've finished the assignment, [Push it](https://github.com/UMD-CS-STICs/389Rfall18/blob/master/HW_Submit_Instructions.md) up to your personal GitHub for us to grade.

Your responses to every prompt in this assignment should include answers to any specific questions along with a brief explanation of your thought process and how you obtained the answer.

### Scoring

Part 1 is worth 45 points, and part 2 is worth 55 points.

### Tips

Reference the slides from lecture 2 to help you effectively utilize available OSINT techniques.
