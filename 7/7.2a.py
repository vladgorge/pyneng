#!/usr/bin/env python3

from sys import argv

name = str(argv[1:]).strip("['']")
file=open(name,'r')


for line in file :
	if line.startswith('!')==False :
		line=str(line).strip('\n')
		if line.find('Current configuration')==-1:
			line=str(line)
			if line.find('duplex')==-1:
				line=str(line)
				if line.find('alias')==-1:
					print(line)

