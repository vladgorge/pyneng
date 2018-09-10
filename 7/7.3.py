#!/usr/bin/env python3

file=open('CAM_table.txt','r')
f=file.readlines()

for line in f:
	if line.count('.')==2:
		vlan=line.split()[0]
		mac=line.split()[1]
		intr=line.split()[3]
		
		print('{}  {}  {}'.format(vlan,mac,intr))
