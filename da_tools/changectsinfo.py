#!/usr/bin/python3

import sys
import xml.etree.ElementTree as ET
import datetime,os

def cleaninfo(inputinfo):
	info=list(filter(lambda x:x!='null',set(inputinfo.split(','))))
	return info[-1]


org=sys.argv[1]
tree = ET.parse(org)
root = tree.getroot()
DeviceInfo=root.find('DeviceInfo')
for child in DeviceInfo:
	if child.tag == 'PhoneSubInfo':
		child.attrib['subscriberId']=cleaninfo(child.attrib['subscriberId'])
	if child.tag == 'BuildInfo':
		child.attrib['deviceID']=cleaninfo(child.attrib['deviceID'])
		child.attrib['imei']=cleaninfo(child.attrib['imei'])
		child.attrib['imsi']=cleaninfo(child.attrib['imsi'])
tree.write('temp.xml',encoding= "UTF-8")
first=open(org,mode='r',encoding= "UTF-8").readline()	
newfile=open(org,mode='w',encoding="UTF-8")
newfile.write(first)
newfile.write(open('temp.xml' ,mode='r',encoding="UTF-8").read())
newfile.close()
os.remove('temp.xml')
print(' finish ')


	
