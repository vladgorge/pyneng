#!/usr/bin/env python3
'''
Задание 18.4

Обновить файл get_data из задания 18.2 или 18.2a.
Добавить поддержку столбца active, который мы добавили в задании 18.3.

Теперь, при запросе информации, сначала должны отображаться активные записи,
а затем, неактивные.

Например:
$ python get_data.py ip 10.1.10.2

Detailed information for host(s) with ip 10.1.10.2
----------------------------------------
mac         : 00:09:BB:3D:D6:58
vlan        : 10
interface   : FastEthernet0/1
switch      : sw1
----------------------------------------

----------------------------------------
Inactive values:
----------------------------------------
mac         : 00:09:23:34:16:18
vlan        : 10
interface   : FastEthernet0/4
switch      : sw1
----------------------------------------

$ python get_data1.py
--------------------------------------------------------------------------------
Active values:
--------------------------------------------------------------------------------
00:09:BB:3D:D6:58  10.1.10.2         10    FastEthernet0/1    sw1         1
00:04:A3:3E:5B:69  10.1.5.2          5     FastEthernet0/10   sw1         1
00:05:B3:7E:9B:60  10.1.5.4          5     FastEthernet0/9    sw1         1
00:07:BC:3F:A6:50  10.1.10.6         10    FastEthernet0/3    sw1         1
00:09:BC:3F:A6:50  192.168.100.100   1     FastEthernet0/7    sw1         1
00:B4:A3:3E:5B:69  10.1.5.20         5     FastEthernet0/5    sw2         1
00:C5:B3:7E:9B:60  10.1.5.40         5     FastEthernet0/9    sw2         1
00:A9:BC:3F:A6:50  10.1.10.60        20    FastEthernet0/2    sw2         1
--------------------------------------------------------------------------------
Inactive values:
--------------------------------------------------------------------------------
00:A9:BB:3D:D6:58  10.1.10.20        10    FastEthernet0/7    sw2         0

'''
import sqlite3
import sys

db_filename = 'dhcp_snooping.db'

if len(sys.argv)==1:
	
	conn = sqlite3.connect(db_filename)

	#Позволяет далее обращаться к данным в колонках, по имени колонки
	#conn.row_factory = sqlite3.Row

	print('В таблице dhcp такие записи:')
	print('-' * 40)

		
	query = 'select * from dhcp'
	result = conn.execute(query)
	for row in result:
		list_1=[]
		for values in row:
			list_1.append(values)
		mac, ip, vlan, intf, devname = list_1
		print('{:10} {:15} {:2} {:18} {:10}'.format(mac, ip, vlan, intf, devname))
		#print('-' * 40)
		
elif len(sys.argv)==3:
	key, value = sys.argv[1:]
	correct_keys=['mac', 'ip', 'vlan', 'interface']
	if key in correct_keys:
		keys = ['mac', 'ip', 'vlan', 'interface']
		keys.remove(key)
		conn = sqlite3.connect(db_filename)
		#Позволяет далее обращаться к данным в колонках, по имени колонки
		conn.row_factory = sqlite3.Row

		print('\nDetailed information for host(s) with', key, value)
		print('-' * 40)

		query = 'select * from dhcp where {} = ?'.format(key)
		result = conn.execute(query, (value, ))

		for row in result:
			for k in keys:
				print('{:12}: {}'.format(k, row[k]))
			print('-' * 40)
	else:
		print('''Данный параметр не поддерживается.\nДопустимые значения параметров: mac, ip, vlan, interface, switch''')
else:
	print('Пожалуйста, введите два или ноль аргументов')
