#!/usr/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse('6768.conf')
root = tree.getroot()

wanip1 = 'WANIPConnection'
#ip = root.getchildren('InternetGatewayDevice/WANDevice[1]/WANConnectionDevice[2]:ExternalIPAddress');
#sub = root.getchild('InternetGatewayDevice/WANDevice instance="1"/WANConnectionDevice instance="2":SubnetMask')
#dg = root.getchild('InternetGatewayDevice/WANDevice instance="1"/WANConnectionDevice instance="2":DefaultGateway')

for child in root.iter('ExternalIPAddress'):
    print(child.tag, child.text)

for child in root:
    for element in child:
        print (element.tag, ":", element.attrib)

#DslCpeConfig > InternetGatewayDevice > WANDevice instance="1" > WANConnectionDevice instance="2" > WANIPConnection instance"1" > ExternalIPAddress, SubnetMask, DefaultGateway
currentip = ip.get("text");

for child in root:
    print(currentip)

#tree.write('out.xml')
