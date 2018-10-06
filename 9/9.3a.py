#!/usr/bin/env python3

def get_int_vlan_map(file):
	f=open(file)
	access={}
	trunk={}
	for line in f:
		if 'interface' in line and 'Eth' in line:
			intf=line.split()[1]
		elif 'access' in line and 'vlan' in line:
			vlan=line.split()[3]
			access[intf]=vlan
		elif 'trunk' in line and 'vlan' in line:
			vlan=line.split()[4]
			trunk[intf]=vlan
		elif 'switchport mode access' in line:
			vlan=1
			access[intf]=vlan
	print(access)
	print(trunk)
	
		
get_int_vlan_map('config_sw2.txt')
