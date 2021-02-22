# usage = python read_snmp_info.py community OID
# Example = python read_snmp_info.py public .1.3.6.1.2.1.1.1.0

from snmp_helper import snmp_get_oid,snmp_extract
import time
import sys

try:
	community_string = str(sys.argv[1])
	oid_string = str(sys.argv[2])
except:
	print('Usage: python read_snmp_info.py public .1.3.6.1.2.1.1.1.0')
	sys.exit()

snmp_port = 161
devices_list = ['']
line_count = 0
timestr = time.strftime('%d%m%Y-%H%M%S')

with open("devices_list.txt") as file:
	for line in file:
		line_count += 1
		line = line.strip()
		devices_list.append(line)
line_count +=1

for x in range(1,line_count):
	try:
		device = (devices_list[x], community_string, snmp_port)
		snmp_data = snmp_get_oid(device, oid_string, display_errors=True)
		print ('\n', devices_list[x])
		output = snmp_extract(snmp_data)
		print(output)
		log = open('oid-' + oid_string + '-' + timestr + '.txt','a')
		log.write('\n')
		log.write(devices_list[x])
		log.write('\n')
		log.write(output)
		log.write('\n')
	except:
		log = open('oid-' + oid_string + '-' + timestr + '.txt','a')
		log.write('\n')
		log.write(devices_list[x])
		log.write('\nDevice inaccessible')
		log.write('\n')
		print ('Device inaccessible')
