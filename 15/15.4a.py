#!/usr/bin/env python3

import re
from parse_sh_ip_int_br import parse_sh_ip_int_br

def convert_to_dict(list, name_list):
	print(list)
	print(name_list)

z



names=['Interface','IP-Address','Status','Protocol']

convert_to_dict(parse_sh_ip_int_br, names)
