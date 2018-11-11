#!/usr/bin/env python3

from draw_network_graph import draw_topology
import yaml

def dict_yaml_to_dict_topology(yaml_file):
	dict_topology={}
	for devname, value in yaml_file.items():
		for localint, value in value.items():
			list_1=[]
			list_1.append(devname)
			list_1.append(localint)
			tuple_1=tuple(list_1)
			for devid, portid in value.items():
				list_2=[]
				list_2.append(devid)
				list_2.append(portid)
				tuple_2=tuple(list_2)
				dict_topology[tuple_1]=tuple_2
	return dict_topology

def check_double_links(dict_topology):
	values_list=[]
	for key in dict_topology.copy().keys():
		for value in dict_topology.copy().values():
			if key==value:
				del(dict_topology[key])
	return dict_topology





file=open('topology.yaml')
f=yaml.load(file)


topology_dict=check_double_links(dict_yaml_to_dict_topology(f))
draw_topology(topology_dict, out_filename='img/topology')



