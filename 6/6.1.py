#!/usr/bin/env python3

ip=input('Введите IP адрес: ')
#ip='10.24.1.10'
IP=ip.split('.')
if (int(IP[0]) < 224)and(int(IP[1])>0):
    print('unicast')
elif (int(IP[0])>=224)and(int(IP[3])<255):
    print('multicast')
elif (int(IP[0])==255)and(int(IP[1])==255)and(int(IP[2])==255)and(int(IP[3])==255):
    print('localbroadcast')
elif (int(IP[0])==0)and(int(IP[1])==0)and(int(IP[2])==0)and(int(IP[3])==0):
    print('unnasigned')
else :
    print('unused')
