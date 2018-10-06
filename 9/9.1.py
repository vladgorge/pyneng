#!/usr/bin/env python3

access={'FastEthernet0/12':10,
'FastEthernet0/14':11,
'FastEthernet0/16':17,
'FastEthernet0/17':150}



def access_template(intf_dict):
	out=[]
	access_temp=['interface',
	'switchport mode access',
	'switchport access vlan',
	'switchport nonegotiate',
	'spanning-tree portfast',
	'spanning-tree bpduguard enable']
	for intf in intf_dict:
		for command in access_temp:
			if command.startswith('interface'):
				out.append('inteface {}'.format(intf))
			elif command.endswith('vlan'):
				out.append('switchport access vlan {}'.format(intf_dict[intf]))
			else:
				out.append(command)
	print(out)
access_template(access)
