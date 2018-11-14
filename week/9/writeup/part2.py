#!/usr/bin/env python
#-*- coding:utf-8 -*-
# importing useful libraries -- feel free to add any others you find necessary

import socket
import hashlib
import re

host = "142.93.117.193"   # IP address or URL
port =  7331    # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024)
print(data)

while (1):
    if 'Find me the' in data:
        value = re.findall("Find me the (?P<type>\S*) hash of (?P<value>\S*)", data)
        hash = hashlib.new(value[0][0])
        hash.update(value[0][1])
        print("Sending the hash " +hash.hexdigest() +'\n')
        s.send(hash.hexdigest() +'\n')
    else:
        break
    data = s.recv(1024)
    print(data)
    
    #line = data.strip().split()
    #if "sha1" in line:
     #   h = hashlib.sha1(line[line.index("of")])
      #  h = h.hexdigest()
    #elif "sha224" in line:
     #   h = hashlib.sha224(line[line.index("of")])
      #h = h.hexdigest()
    

# close the connection
s.close()
