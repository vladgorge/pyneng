#!/usr/bin/env python

def create_db(db_filename, schema_filename):
	import os
	import sqlite3
	db_filename = 'dhcp_snooping.db'
	schema_filename = 'dhcp_snooping_schema.sql'
	db_exists = os.path.exists(db_filename)
	conn = sqlite3.connect(db_filename)

	if not db_exists:
		print('Creating schema...')
		with open(schema_filename, 'r') as f:
			schema = f.read()
		conn.executescript(schema)
		print('Done')
	else:
		print('Database exists, assume dhcp table does, too.')


def add_data(db_filename, filenames):
	import re
	import sqlite3
	import os
	from datetime import timedelta
	import datetime
	regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
	for file in filenames:
		db_exists = os.path.exists(db_filename)
		if db_exists==False:
			print('Please create '+db_filename)
			break
		result = []
		with open(file) as data:
			now = datetime.datetime.today().replace(microsecond=0)
			for line in data:
				match = regex.search(line)
				if match:
					list_1=list(match.groups())
					switch_name=(file.split('_')[0])
					list_1.append(switch_name)
					list_1.append(1)
					list_1.append(now)
					tuple_1=tuple(list_1)
					result.append(tuple_1)
		conn = sqlite3.connect(db_filename)
		for row in conn.execute('select * from dhcp'):
			week_ago = now - timedelta(days=7)
			if str(week_ago)>row[6]:
				delete_query='delete from dhcp where last_active="{}"'.format(row[6])
				conn.execute(delete_query)
		switch_query='update dhcp set active=0 where switch="{}"'.format(switch_name)
		conn.execute(switch_query)
		for row in result:
			try:
				with conn:
					query = '''insert or replace into dhcp (mac, ip, vlan, interface, switch, active, last_active)
							values (?, ?, ?, ?, ?, ?, ?)'''
					conn.execute(query, row)
			except sqlite3.IntegrityError as e:
				print('Error occured: ', e)
		conn.close()   
			 
def add_data_switches(db_filename, filename):
	import sqlite3
	import yaml
	file=open(str(filename).strip("['']"))
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

def get_all_data(db_filename):
	import sqlite3
	import sys

	db_filename = 'dhcp_snooping.db'
	conn = sqlite3.connect(db_filename)

	query = 'select * from dhcp where active=1'
	result = conn.execute(query)
	print('Active values:')
	print('-' * 60)	
	for row in result:
		list_1=[]
		for values in row:
			list_1.append(values)
		mac, ip, vlan, intf, devname, active, last_active = list_1
		print('{:10} {:15} {:2} {:18} {:10} {:2} {:15}'.format(mac, ip, vlan, intf, devname, active, last_active))
	print('-' * 60)
	
	query = 'select * from dhcp where active=0'
	result = conn.execute(query)
	print('Inactive values:')
	print('-' * 60)	
	for row in result:
		list_1=[]
		for values in row:
			list_1.append(values)
		mac, ip, vlan, intf, devname, active, last_active = list_1
		print('{:10} {:15} {:2} {:18} {:10} {:2} {:15}'.format(mac, ip, vlan, intf, devname, active, last_active))
	print('-' * 60)

def get_data(db_filename, key, value):
	import sqlite3
	import sys	
	correct_keys=['mac', 'ip', 'vlan', 'interface']
	if key in correct_keys:
		keys = ['mac', 'ip', 'vlan', 'interface']
		keys.remove(key)
		conn = sqlite3.connect(db_filename)
		conn.row_factory = sqlite3.Row

		print('Detailed information for host(s) with {} {}'.format(key, value))
		print('-' *40)

		query = 'select * from dhcp where active=1 and {} = ?'.format(key)
		result = conn.execute(query, (value, ))

		for row in result:
			for k in keys:
				print('{:12}: {}'.format(k, row[k]))
			print('-' * 40)
			
		query = 'select * from dhcp where active=0 and {} = ?'.format(key)
		result = conn.execute(query, (value, ))
		print('Inactive values:')
		print('-' * 40)
		for row in result:
			for k in keys:
				print('{:12}: {}'.format(k, row[k]))
			print('-' * 40)			


