#!/usr/bin/env python

from pprint import pprint
from jnpr.junos import Device
from getpass import getpass

dev = Device(host='100.100.100.100', user='auto', ssh_private_key_file="JUNOS_auto_id_rsa")
dev.open() 
pprint(dev.facts)
dev.close()
