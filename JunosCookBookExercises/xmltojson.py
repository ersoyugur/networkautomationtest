#!/usr/bin/env python


import xml.dom.minidom as minidom

tree=minidom.parse('test.xml')
nodes=tree.documentElement
books=tree.getElementsByTagName("name")

serials = []
for sn in books:
	snobj=sn.getElementsByTagName('description')
	serials.append(snobj)

print serials 
