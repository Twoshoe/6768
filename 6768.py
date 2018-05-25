#!/usr/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse('6768.conf')
root = tree.getroot()

#for X_BROADCOM_COM_CONNECTIONMODE in root.findall('X_BROADCOM_COM_CONNECTIONMODE'):
#    ip = X_BROADCOM_COM_CONNECTIONMODE.find('ExternalIPAddress').text
#    subnet = X_BROADCOM_COM_CONNECTIONMODE.get('SubnetMask')
#    defaultgw = X_BROADCOM_COM_CONNECTIONMODE.get('DefaultGateway')
#    print(ip, subnet, defaultgw)

tree.write('out.xml')




