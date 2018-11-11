#!/usr/bin/env python3
'''
Задание 18.1

add_data.py
* с помощью этого скрипта, выполняется добавление данных в БД
* добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах


В файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
'''




import glob

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
yaml_filename = 'switches.yml'

def add_data_txt(dhcp_snoop_files):
	import re
	import sqlite3
	regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
	for file in dhcp_snoop_files:
		result = []
		with open(file) as data:
			for line in data:
				match = regex.search(line)
				if match:
					list_1=list(match.groups())
					list_1.append(file.split('_')[0])
					tuple_1=tuple(list_1)
					result.append(tuple_1)
		conn = sqlite3.connect(db_filename)
		for row in result:
			try:
				with conn:
					query = '''replace into dhcp (mac, ip, vlan, interface, switch)
							values (?, ?, ?, ?, ?)'''
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
				query = '''replace into switches (hostname, location)
						values (?, ?)'''
				conn.execute(query, row)
		except sqlite3.IntegrityError as e:
			print('Error occured: ', e)
	conn.close()

		
add_data_yaml(yaml_filename)	
add_data_txt(dhcp_snoop_files)	












