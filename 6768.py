#!/usr/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse('6768.conf')
root = tree.getroot()

wanip1 = 'WANIPConnection instance="1"'
ip = ExternalIPAddress
sub = SubnetMask
dg = DefaultGateway

#for X_BROADCOM_COM_CONNECTIONMODE in root.findall('X_BROADCOM_COM_CONNECTIONMODE'):
#    ip = X_BROADCOM_COM_CONNECTIONMODE.find('ExternalIPAddress').text
#    subnet = X_BROADCOM_COM_CONNECTIONMODE.get('SubnetMask')
#    defaultgw = X_BROADCOM_COM_CONNECTIONMODE.get('DefaultGateway')
#    print(ip, subnet, defaultgw)

for child in root.iter('WANIPConnection instance="1"'):
    print(SubnetMask.attrib)


tree.write('out.xml')
