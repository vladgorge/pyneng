#!/usr/bin/env python3

def parse_sh_cdp_neighbors(command):
	import re
	devname=re.search('(.{2,})>', command)
	string=re.finditer('(\S+)\s +(Eth \S+)\s +\d+\s +(\S\s)+ \s + (\S+)\s+(Eth \S+)\s', command)
	dict_cdp={}
	dict_cdp[devname.group(1)]={}

	for match in string:
		dict_cdp[devname.group(1)][match.group(2)]={}
		dict_cdp[devname.group(1)][match.group(2)][match.group(1)]=match.group(5)
	print(dict_cdp)
	

f=open('sh_cdp_n_r4.txt')
output=f.read()
parse_sh_cdp_neighbors(output)
