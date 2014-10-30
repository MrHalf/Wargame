#!/usr/bin/python
 
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(('semtex.labs.overthewire.org', 24000))
f=open('elf32','wb')
i=1
while True :
    data = s.recv(1)
    if i % 2 != 0:
        if data:
            f.write(data)
        else:
            break
    i += 1
