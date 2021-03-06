#!/usr/bin/env python3

access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk allowed vlan {}']

mode=input('Interface mode (access/trunk):')
modevlan={
'access' : 'Enter VLAN numbers:',
'trunk' : 'Enter allowed VLANs:'
}
interface=input('Interface: ')

vlan=input((modevlan[mode]))

modedict={
'access' : access_template,
'trunk' : trunk_template
}


print('\n'+'-'*30)
print('interface '+interface)
print('\n'.join(modedict[mode]).format(vlan))
