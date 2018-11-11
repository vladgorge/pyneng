#!/usr/bin/env python3

def parse_sh_version(output):
	import re
	ios=re.search('Version (.+),', output)
	image=re.search('image file is (.+)', output)
	uptime=re.search('uptime is (.+)', output)
	list_1=[]
	list_1.append(ios.group(1))
	list_1.append(image.group(1))
	list_1.append(uptime.group(1))
	tuple_1=tuple(list_1)
	return tuple_1

def write_to_csv(filename, list):
	import csv
	with open(filename, 'w') as f:
		writer = csv.writer(f)
		for row in list:
			writer.writerow(row)
	


import glob

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)
headers = ['hostname', 'ios', 'image', 'uptime']
	
data_1=[]
data_1.append(headers)

for file in sh_version_files:
	f=open(file)
	output=f.read()
	data_2=[]
	data_2.append(str(file).split('_')[2].split('.')[0])
	data_2.extend(parse_sh_version(output))
	data_1.append(data_2)
print(data_1)	
	
filename='sw_data_new.csv'	
write_to_csv(filename, data_1)
