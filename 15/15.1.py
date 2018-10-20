#!/usr/bin/env python3


ip_address=['10.1.1.0', '8.8.8.8']

def check_ip_addresses(ip_address):
	import	subprocess
	reachable_list=[]
	unreachable_list=[]
	
		
	for ip in ip_address:
		result = subprocess.run(['ping', '-c', '3', '-n', ip], stdout=subprocess.PIPE)
		result=result.stdout
		if str(result).count('3 received')==1:
			reachable_list.append(ip)
		elif str(result).count('3 received')==0:
			unreachable_list.append(ip)
	return unreachable_list, reachable_list

	'''if __name__ == "__main__":			
		print(reachable_list)
		print(unreachable_list)'''
		
if __name__ == "__main__":		
	print(check_ip_addresses(ip_address))

