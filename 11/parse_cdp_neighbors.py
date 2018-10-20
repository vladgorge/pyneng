#!/usr/bin/env python3

def parse_cdp_neighbors(input_txt):
	f=open(input_txt)
	devname=f.readline().split('>')[0]
	f1=f.readlines()[4:]
	dict_neighbors={}
	for line in f1:
		devid=line.replace('Eth ','Eth').replace(' S ','S').split()[0]
		locint=line.replace('Eth ','Eth').replace(' S ','S').split()[1]
		portid=line.replace('Eth ','Eth').replace(' S ','S').split()[5]
		dict_neighbors.setdefault(tuple([devname,locint]))
		dict_neighbors[tuple([devname,locint])]=tuple([devid,portid])
	return dict_neighbors
	print(dict_neighbors)
		
		

		
#parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt')	
		
		

'''{('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
('R4', 'Fa0/2'): ('R6', 'Fa0/0')}'''
