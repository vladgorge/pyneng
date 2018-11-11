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
	return dict_cdp

if __name__ == "__main__":
	import glob

	sh_cdp_files = glob.glob('sh_cdp_n*')
	for file in sh_cdp_files:
		f=open(file)
		output=f.read()
		print(parse_sh_cdp_neighbors(output))
	

