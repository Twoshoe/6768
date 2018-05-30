#!/usr/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse('6768.conf')
root = tree.getroot()

wanip1 = 'WANIPConnection'
ip = wanip1.find('ExternalIPAddress')
sub = wanip1.find('SubnetMask')
dg = wanip1.find('DefaultGateway')

for child in root.iter('ExternalIPAddress'):
    print(child.tag, child.text)

for child in root.findall('wanip1'):
    print(ip, sub, dg)

tree.write('out.xml')
