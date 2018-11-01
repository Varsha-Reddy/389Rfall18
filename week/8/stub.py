#!/usr/bin/env python2

import sys
import struct
import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version, timestamp, author, section_count = struct.unpack("<LLL8sL", data[0:24])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %d" % int(timestamp))
print("AUTHOR: %s" % author)
print("SECTION COUNT: %d" % int(section_count))
# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")

start = 24
end = start + 8
i = 1

while(start < len(data)):

    sectionType, sectionLen = struct.unpack("<LL",data[start:start+8])
    sec_start = end
    sec_end = sec_start + sectionLen
    print("#%d Section type:%d Section length:%d" % (i, sectionType, sectionLen))

    if sectionType == 0x1:
        print("SECTION_PNG")
        with open("%d_output.png" % i,"wb") as f:
            f.write(b'\211PNG\r\n\032\n')
            f.write(data[sec_start:sec_end])
    elif sectionType == 0x2:
        print("SECTION_DWORDS")
        doubleW =[]
        for x in range(0, len(data[sec_start: sec_end])/8):
            doubleW.append(data[x*8: x*8+8])
        print(doubleW)
    elif sectionType == 0x3:
        print("SECTION_UFT8")
        x = struct.unpack(str(sectionLen) + "s", data[sec_start: sec_end])
        print("%s" % x)
    elif sectionType == 0x4:
        print("SECTION_DOUBLES")
        x = struct.unpack(str(sectionLen) + "s", data[sec_start: sec_end])
        print("%s" % x)
    elif sectionType == 0x5:
        print("SECTION_WORDS")
        word = []
        for x in range(0, len(data[sec_start: sec_end])/4):
            word.append(data[x*4: x*4+4])
        print(word)
    elif sectionType == 0x6:
        print("SECTION_COORD")
        x,y = struct.unpack("<dd", data[sec_start: sec_end])
        print("latitude %s longitude %s" %(str(x), str(y)))
    elif sectionType == 0x7:
        print("SECTION_REFERENCE")
        print("reference %d" %(struct.unpack("<L", data[sec_start: sec_end])))
    elif sectionType == 0x9:
        print("SECTION_ASCII")
        print(data[sec_start: sec_end])
    else:
        print("Error")

    f = open("section %d" % (int(sectionType)), "w")
    f.write(data[sec_start: sec_end])
    print("\n")
    start += sectionLen + 8
    i += 1
