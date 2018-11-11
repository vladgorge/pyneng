#!/usr/bin/env python3


def add_data_txt(dhcp_snoop_files):
	import re
	import sqlite3
	import os
	regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
	for file in dhcp_snoop_files:
		db_exists = os.path.exists(db_filename)
		if db_exists==False:
			print('Please create '+db_filename)
			break
		result = []
		with open(file) as data:
			for line in data:
				match = regex.search(line)
				if match:
					list_1=list(match.groups())
					switch_name=(file.split('_')[0])
					list_1.append(switch_name)
					list_1.append(1)
					tuple_1=tuple(list_1)
					result.append(tuple_1)
		conn = sqlite3.connect(db_filename)
		switch_query='update dhcp set active=0 where switch="{}"'.format(switch_name)
		print(switch_query)
		conn.execute(switch_query)
		for row in result:
			try:
				with conn:
					query = '''insert or replace into dhcp (mac, ip, vlan, interface, switch, active)
							values (?, ?, ?, ?, ?, ?)'''
					conn.execute(query, row)
			except sqlite3.IntegrityError as e:
				print('Error occured: ', e)
		conn.close()

def add_data_yaml(yaml_filename):
	import yaml
	import sqlite3
	file=open(yaml_filename)
	f=yaml.load(file)
	switches=[]
	for value in f.values():
		for hostname, location in value.items():
			list_2=[]
			list_2.append(hostname)
			list_2.append(location)
			switches.append(tuple(list_2))
	conn = sqlite3.connect(db_filename)
	for row in switches:
		try:
			with conn:
				query = '''insert into switches (hostname, location)
						values (?, ?)'''
				conn.execute(query, row)
		except sqlite3.IntegrityError as e:
			print('Error occured: ', e)
	conn.close()

import glob

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
yaml_filename = 'switches.yml'
		
#add_data_yaml(yaml_filename)	
add_data_txt(dhcp_snoop_files)	












