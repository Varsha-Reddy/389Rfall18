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
First, I ran the command "objdump -D binary". It disassembled everything and helped me view the binary file in assembly form. But, it didn't give me any useful information or clues on how to proceed to get the flag. Second, I used radare2 to reverse engineer. I had to do some reading to familiarize myself with radare2. I ran the "aa" command to "analyze all". Next I used the "aaa" and "aac" to analyze function calls. I didn't find anything useful. I used the "s" command that is used to seek a memory spot with a function name. I knew the main function would have code, so I ran the command "s main". To view the contents, I did "pdf". At the beginning of the main function, I noticed, "/tmp/.stego" aligned vertically. To check the directories contents, I exited radare2 and ran "./binary" which displayed the message "Where is your flag?". Then I did "cd /tmp".
On listing, I could see a couple of directories. I navigated into the first one: "ssh-zLKXmlHFJKcB" and displayed "agent.824". When I viewed agent.824 it displayed "Image Magick".
Then I realized that stego was a hidden file and to list it, I did "ls -a". To check the stego's file type I used binwalk. It was a JPEG image data format. Going by the files name, I knew I had to use steganographic analysis techniques. I ran "steghide extract -sf stego". This prompted me to enter a passphrase. After several failed attempts of trying to guess the passphrase, I figured I had to look around to find a clue about the passphrase. I tried to use techniques that I used for the first part of the assignment such as "binwalk --dd "jpeg:jpeg" .stego " This created an extracted directory with an image of a "Stegosaurus" in it. 
I went back and tried using it as the paraphrase. It didn't work. I figured that I need to create a text file to extract the data to. So Lastly, I executed the following commands: 

cd _.stego.extracted/ 

steghide extract -sf 1.jpeg -xf output.txt (wrote extracted data to output.txt)

cat output.txt

FLAG: Congrats! Your flag is: CMSC389R-{dropping_files_is_fun}



 
