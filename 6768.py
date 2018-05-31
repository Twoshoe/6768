#!/usr/bin/env python3

'''Generate configuration files for an arbitrary range of IP addresses.'''

import xml.etree.ElementTree as ET
import argparse
from os import mkdir, path


TREE = ET.parse('6768.conf')
ROOT = TREE.getroot()
OUTPUT_DIR = 'configs'

PARSER = argparse.ArgumentParser(description='Generate configuration files')
PARSER.add_argument('IP_BASE', metavar='Base', type=str, nargs=1,
        help='IP prefix (e.g. 10.60.1)')
PARSER.add_argument('IP_START', metavar='Start', type=int, nargs=1,
        help='Beginning of IP range (e.g. 10)')
PARSER.add_argument('IP_END', metavar='End', type=int, nargs=1,
        help='End of IP range (e.g. 245)')

ARGS = PARSER.parse_args()

try:
    mkdir(OUTPUT_DIR)
except FileExistsError:
    pass

# Moves down through the Element Tree to get to ExternalIPAddress, Subnet, Default Gateway
for child in ROOT.iter('ExternalIPAddress'):
    if child.text:
        for i in range(ARGS.IP_START[0], ARGS.IP_END[0] + 1):
            new_ip = ARGS.IP_BASE[0] + '.' + str(i)

            # This Line sets the IP Address to whatever value is given.
            child.text = new_ip
            conf = path.join(OUTPUT_DIR, '6768-' + str(i) + '.conf')
            TREE.write(conf)
