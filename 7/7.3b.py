#!/usr/bin/env python3

file=open('CAM_table.txt','r')
f=file.readlines()

out=[]

for line in f:
	if line.count('.')==2:
		vlan=line.split()[0]
		mac=line.split()[1]
		intr=line.split()[3]
		string=vlan+'  '+mac+'  '+intr
		out.append(string)
		out.sort()
vlanid=input('Введите VLAN: ')
		
for line in out:
	if line.startswith(vlanid):
		print(line.strip("['']"))

