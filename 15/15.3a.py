#!/usr/bin/env python3

import re

regex=('interface +(?P<intr>\S+)'
'|ip address +(\d+\.\d+\.\d+\.\d+) +(\d+\.\d+\.\d+\.\d+)')
result={}
f=open('config_r1.txt')
ip_addresses=re.finditer(regex,f.read())
for match in ip_addresses:
	if match.lastgroup == 'intr':
		intr = match.group(match.lastgroup)
		result[intr] = {}
	elif intr:
		result[intr]=match.group(2,3)

for key, value in result.copy().items():
	if not value:
		del(result[key])

print(result)



