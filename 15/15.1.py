#!/usr/bin/env python3

from sys import argv
import re

log_file, regex = argv[1:]
f=open(log_file)
regex_part=regex.split()
for regex in regex_part:
	for line in f:
		if re.match('FastEthernet{} '.format(regex),line):
			print(line.strip())
	f.seek(0)
