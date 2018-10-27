#!/usr/bin/env python3

import re

def return_match(log_file, regex):
	f=open(log_file)
	list_1=[]
	for line in f:
		aaa=re.search(regex,line)
		if aaa:
			list_1.append(aaa.group())
	print(list_1)

regex=input("Введите : ")
log_file="sh_ip_int_br.txt"
return_match(log_file, regex)
