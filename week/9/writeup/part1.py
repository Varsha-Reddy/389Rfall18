#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
hashlist = open('../hashes','r').read().split()
wordlist = open("../probable-v2-top1575.txt", 'r')
# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

for hash in hashlist:
    hash = hash.strip()
    for word in wordlist:
        for salt in salts:
            password = hashlib.sha512(salt + word.rstrip()).hexdigest()
            if password in hashlist:
                print "Password: " + word.strip() 
                print "Salt: " + salt
