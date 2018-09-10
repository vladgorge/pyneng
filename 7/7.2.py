#!/usr/bin/env python3

from sys import argv

name = str(argv[1:]).strip("['']")
file=open(name,'r')
f=file.read().split('\n')
for line in f :
	if line.startswith('!')==False :
		print(line)
