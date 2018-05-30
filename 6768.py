#!/usr/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse('6768.conf')
root = tree.getroot()
CommitChanges = False

for WANDevice in root.find('InternetGatewayDevice').findall('WANDevice'):
    if 'instance' not in WANDevice.attrib:
        continue
    if (WANDevice.attrib['instance'] == '1'):
        for WANConnectionDevice in WANDevice.findall('WANConnectionDevice'):
            if 'instance' not in WANConnectionDevice.attrib:
                continue
            if (WANConnectionDevice.attrib['instance'] == '2'):
                for WANIPConnection in WANConnectionDevice.findall('WANIPConnection'):
                    if 'instance' not in WANIPConnection.attrib:
                        continue
                    if (WANIPConnection.attrib['instance'] == '1'):
                        print(WANIPConnection.find('ExternalIPAddress').text, WANIPConnection.find('SubnetMask').text, WANIPConnection.find('DefaultGateway').text)
                        WANIPConnection.find('ExternalIPAddress').text = '10.60.1.10'
                        CommitChanges = True
                        ip_base = '10.60.1.' 
                        ip_start = 10
                        for (i = ip_start; i < 245; i++) {
                                    new_ip = ip_base + i.toString()
                                        change_ip(new_ip)
                                        }
                            if (CommitChanges):
                                tree.write('out.xml')

#This was to print part of the tree
#for child in root:
#   for element in child:
#        print (element.tag, ":", element.attrib)

#This is the path to the external IP address
#DslCpeConfig > InternetGatewayDevice > WANDevice instance="1" > WANConnectionDevice instance="2" > WANIPConnection instance"1" > ExternalIPAddress, SubnetMask, DefaultGateway

