#!/usr/bin/env python3

trunk={ 'FastEthernet0/1':[10,20],
'FastEthernet0/2':[11,30],
'FastEthernet0/4':[17] }



def trunk_template(intf_dict):
	out=[]
	trunk_temp=['switchport trunk encapsulation dot1q',
	'switchport mode trunk',
	'switchport trunk native vlan',
	'switchport trunk allowed vlan']
	for intf in intf_dict:
		for command in trunk_temp:
			if command.endswith('native vlan'):
				out.append('switchport trunk native vlan {}'.format(str(intf_dict[intf]).strip('[]')))
			else:
				out.append(command)
	print(out)
	
trunk_template(trunk)
