#!/usr/bin/env python3

import re

regex=(' ip address +(\d+\.\d+\.\d+\.\d+) +(\d+\.\d+\.\d+\.\d+)')
groups=[]
f=open('config_r1.txt')
ip_addresses=re.finditer(regex,f.read())
for match in ip_addresses:
	print(match)
	groups.append(match.groups())
print(groups)
