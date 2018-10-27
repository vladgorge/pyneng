#!/usr/bin/env python3

import re

def parse_sh_ip_int_br(log_file):

	f=open(log_file)
	result = re.finditer('(\S+) +'
	'([\d.]+) +'
	'\w+ +\w+ +'
	'(up|down|administratively down) +'
	'(up|down)', f.read())
	groups=[]
	for match in result:
		groups.append(match.groups())
	return groups

if __name__ == "__main__":
	print(parse_sh_ip_int_br('sh_ip_int_br_2.txt'))
