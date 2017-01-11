#!/usr/bin/python3

import sys
import xml.etree.ElementTree as ET
import datetime,os
old=datetime.datetime.now()
org=sys.argv[1]
tree = ET.parse(org)
root = tree.getroot()
for child in root:
	if child.tag == 'TestPackage':
		child.clear()
tree.write('temp.xml',encoding= "UTF-8")
first=open(org,mode='r',encoding= "UTF-8").readline()	
newfile=open(os.path.abspath(os.path.dirname(org))+'/info.xml',mode='w',encoding= "UTF-8")
newfile.write(first)
newfile.write(open('temp.xml' ,mode='r',encoding="UTF-8").read())
newfile.close()
os.remove('temp.xml')
print('finish')

