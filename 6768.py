#!/usr/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse('6768.conf')
root = tree.getroot()

wanip1 = 'WANIPConnection instance"1"'
ip = wanip1.find('ExternalIPAddress')
sub = wanip1.find('SubnetMask')
dg = wanip1.find('DefaultGateway')

#for X_BROADCOM_COM_CONNECTIONMODE in root.findall('X_BROADCOM_COM_CONNECTIONMODE'):
#    ip = X_BROADCOM_COM_CONNECTIONMODE.find('ExternalIPAddress').text
#    subnet = X_BROADCOM_COM_CONNECTIONMODE.get('SubnetMask')
#    defaultgw = X_BROADCOM_COM_CONNECTIONMODE.get('DefaultGateway')
#    print(ip, subnet, defaultgw)

#for child in root.iter('WANIPConnection instance="1"'):
#    print(SubnetMask.attrib)

for child in root.findall('wanip1'):
    print(ip, sub, dg)

tree.write('out.xml')
