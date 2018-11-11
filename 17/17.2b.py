#!/usr/bin/env python3

def generate_topology_from_cdp(list_of_files, save_to_file=True, topology_filename='topology.yaml'):
	import yaml
	from parse_sh_cdp_neighbors import parse_sh_cdp_neighbors
	topology={}
	for file in list_of_files:
		f=open(file)
		output=f.read()
		for key, value in parse_sh_cdp_neighbors(output).items():
			topology[key]=value
	with open(topology_filename, 'w') as f:
		yaml.dump(topology, f)
	with open(topology_filename) as f:
		print(f.read())
	return topology

import glob
sh_cdp_files = glob.glob('sh_cdp_n*')
generate_topology_from_cdp(sh_cdp_files, save_to_file=True, topology_filename='topology.yaml')
