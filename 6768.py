#!/usr/bin/env python3

import xml.etree.ElementTree as ET

TREE = ET.parse('6768.conf')
ROOT = TREE.getroot()
IP_BASE = '10.60.1.'
IP_START = 10
IP_END = 246

# Moves down through the Element Tree to get to ExternalIPAddress, Subnet, Default Gateway
for WANDevice in ROOT.find('InternetGatewayDevice').findall('WANDevice'):
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
                        # Iterates on the IP Address between 10 and 245 and saves each IP as a new file.
                        for i in range(IP_START, IP_END):
                            new_ip = IP_BASE + str(i)

                            # This Line sets the IP Address to whatever value is given.
                            WANIPConnection.find('ExternalIPAddress').text = new_ip
                            print(new_ip)
                            # TREE.write('out.xml')

# This was to print part of the tree
# for child in root:
#   for element in child:
#        print (element.tag, ":", element.attrib)

# This is the path to the external IP address
# DslCpeConfig > InternetGatewayDevice > WANDevice instance="1" > WANConnectionDevice instance="2" > WANIPConnection instance"1" > ExternalIPAddress, SubnetMask, DefaultGateway
