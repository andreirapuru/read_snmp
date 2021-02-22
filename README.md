# Read SNMP OID
Read SNMP Info (specified OIDs) from Routers and Switches, and save the output in a .txt file.

# Requires
- Python (tested on Python 3.8.6)
- Modules
  - snmp helper
  - time
  - sys
- You can use pip install -r requirements.txt to install all modules

# Supports
Routers and Switches Cisco with SNMP version 2c community configured

# Limitations
- Same community for all devices in devices_list.txt
- Works for SNMP version 2c
- Run on port UDP/161, if necessary you can chance that on code (snmp_port = your_port)

# Usage
1) Install Python and the modules
2) Download this repository or copy read_snmp_oid.py, snmp_helper.py and devices_list.txt to the same folder
3) Run "python read_snmp_oid.py community OID (Ex. python read_snmp_info.py brainwork .1.3.6.1.2.1.1.5.0)
[output](https://user-images.githubusercontent.com/17407109/108751337-d6517d00-7520-11eb-900c-eb6ac201abd7.PNG)

# Use case
To collect specific SNMP information for a list of devices

# Getting Help
If you are having trouble or need help, create an issue [here](https://github.com/andreirapuru/read_snmp/issues)

# Credits and references
All credits to Kirk Byers for making [SNMP Helper](https://github.com/ktbyers/pynet/blob/master/snmp/snmp_helper.py)
