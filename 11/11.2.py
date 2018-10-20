#!/usr/bin/env python3

import parse_cdp_neighbors
import draw_network_graph

r=parse_cdp_neighbors.parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt')	
draw_network_graph.draw_topology(parse_cdp_neighbors.parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt'))
	

