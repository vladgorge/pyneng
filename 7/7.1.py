#!/usr/bin/env python3

file=open('ospf.txt','r')
out='''
    ...: Protocol: {:15}
    ...: Prefix: {:15}
    ...: AD/Metric {:15}
    ...: Next-Hop: {:15}
    ...: Last Update {:15}
    ...: Outbound Interface: {:15}
    ...: '''

for line in file :
	line=line.replace(',','').replace('via ','').replace('[','').replace(']','').split()
	print(out.format('OSPF', line[1], line[2], line[3], line[4], line[5], ))
