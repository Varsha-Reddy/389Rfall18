#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import struct

host = "142.93.118.186"
port = 1234

message = 'This is a test'    # original message here
malicious = 'Not really'  # put your malicious message here
#####################################
### STEP 1: Calculate forged hash ###
#####################################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.recv(1024)
s.send("1\n")

s.recv(1024)
s.send(message+"\n")
data = s.recv(1024)

data = data.split(' ')
n = data.index('hash:')

# a legit hash of secret + message goes here, obtained from signing a message
legit = data[n + 1].strip()
# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()

print(fake_hash)
data = s.recv(1024)

#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits
strlen = len(message)

for size in range(6,16):
    padding = '\x80'
    for i in range(1, 64 - strlen -size - 8):
        padding += '\x00'
    padding += struct.pack('<Q', (strlen + size)*8)
   
    payload = message + padding + malicious
    s.send("2\n")
    data = s.recv(1024)
    print(data)

    s.send(fake_hash + "\n")
    data = s.recv(1024)
    print(data)

    s.send(payload + "\n")
    data = s.recv(1024)
    print(data)

    if 'Wow' in data:
	print("FLAG FOUND")
	break
s.close()

# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!
