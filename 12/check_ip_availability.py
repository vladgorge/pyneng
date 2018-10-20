#!/usr/bin/env python3

from check_ip_addresses import check_ip_addresses

ip_address=['8.8.8.8', '103.3.1.1-103.3.1.3', '10.2.1.1-10.2.1.5']

def check_ip_availability(ip_address):
	new_list=[]
	for ip in ip_address:
		if ip.count('-')==1 and ip.split('-')[1].count('.')>0:
			first_ip=ip.split('-')[0].split('.')[3]
			last_ip=ip.split('-')[1].split('.')[3]
			ip_network="{}.{}.{}.".format(ip.split('-')[0].split('.')[0],ip.split('-')[0].split('.')[1],ip.split('-')[0].split('.')[2])
			for i in range(int(first_ip), int(last_ip)+1):
				new_list.append(ip_network+str(i))
		elif  ip.count('-')==1 and ip.split('-')[1].count('.')==0:		
			first_ip=ip.split('-')[0].split('.')[3]
			last_ip=ip.split('-')[1]
			ip_network="{}.{}.{}.".format(ip.split('-')[0].split('.')[0],ip.split('-')[0].split('.')[1],ip.split('-')[0].split('.')[2])
			for i in range(int(first_ip), int(last_ip)+1):
				new_list.append(ip_network+str(i))
		else:
			new_list.append(ip)
	ip_address_out=check_ip_addresses(new_list)
	if __name__ == "__main__":
		print(ip_address_out)

check_ip_availability(ip_address)
