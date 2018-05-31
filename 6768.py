#!/usr/bin/env python3

'''Generate configuration files for an arbitrary range of IP addresses.'''

import xml.etree.ElementTree as ET
import argparse

TREE = ET.parse('6768.conf')
ROOT = TREE.getroot()

PARSER = argparse.ArgumentParser(description='Generate configuration files')
PARSER.add_argument('IP_BASE', metavar='Base', type=str, nargs=1,
        help='IP prefix (e.g. 10.60.1)')
PARSER.add_argument('IP_START', metavar='Start', type=int, nargs=1,
        help='IP prefix (e.g. 10)')
PARSER.add_argument('IP_END', metavar='End', type=int, nargs=1,
        help='IP prefix (e.g. 245)')

ARGS = PARSER.parse_args()

print(ARGS)

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
                        for i in range(ARGS.IP_START[0], ARGS.IP_END[0] + 1):
                            new_ip = ARGS.IP_BASE[0] + '.' + str(i)

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
