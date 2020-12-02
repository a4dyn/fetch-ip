# -*- coding: utf-8 -*-

import re

ip_in = open('ip.txt', 'r')
content = ip_in.read()
ip_in.close()

ip_out = []

ip_raw = re.findall(r'\d+\.\d+\.\d+', content, re.M)

for ip in ip_raw:
    ip += '.0/24'
    ip_out.append(ip)

base = open('temp.txt', 'r')
base_content = base.read()
base_list = base_content.split('\n')

result = list(set(ip_out + base_list))

output = open('output.txt', 'w')

for msg in result:
    if msg != '':
        output.write(msg + '\n')

output.close()
