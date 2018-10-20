#!/usr/bin/env python3

import parse_cdp_neighbors
import draw_network_graph
dict_topology={}

dict_list=['r1','r2','r3','sw1']
for filename in dict_list:
	file_name=parse_cdp_neighbors.parse_cdp_neighbors('sh_cdp_n_{}.txt'.format(filename))
	dict_topology.update(file_name)
	for key in dict_topology.copy().keys():
		for value in dict_topology.copy().values():
			if key==value:
				del(dict_topology[key])
				
	
draw_network_graph.draw_topology(dict_topology)

