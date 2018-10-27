#!/usr/bin/env python3

import re

regex=('interface +(?P<intr>\S+)'
'|ip address +(\d+\.\d+\.\d+\.\d+) +(\d+\.\d+\.\d+\.\d+)')
result={}

f=open('config_r2.txt')
ip_addresses=re.finditer(regex,f.read())
for match in ip_addresses:
	if match.lastgroup == 'intr':
		intr = match.group(match.lastgroup)
		result[intr] = {}
		list_1=[]
	elif intr:
		result[intr]=list_1
		list_1.append(match.group(2,3))

for key, value in result.copy().items():
	if not value:
		del(result[key])

print(result)



