#!/usr/bin/env python3

reachable_list=['10.1.1.0','10.1.1.1','10.1.1.2']
unreachable_list=['10.2.1.0','10.2.1.1','10.2.1.2','10.1.1.3']

from tabulate import tabulate
from itertools import zip_longest as zip_longest

def ip_table(list1, list2):
	ip_list=[]
	for ip1,ip2 in zip_longest(list1, list2):
		new_dict={}
		new_dict['Reacheable']=ip1
		new_dict['Unreacheable']=ip2
		ip_list.append(new_dict)

	print(ip_list)
	print(tabulate(ip_list, headers='keys'))
	
ip_table(reachable_list, unreachable_list)







