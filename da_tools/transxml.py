#!/usr/bin/python3

import sys
from lxml import etree
import os

org=sys.argv[1]
evo=sys.argv[2]
tree = etree.parse(evo)
tree1= etree.parse(org)
root = tree.getroot()
root2=tree1.getroot()
for child in root:
    if child.tag == 'TestPackage':
        root2.append(child)
newfile=open(org ,mode='wb')
newfile.write(etree.tostring(tree1,encoding= "UTF-8",pretty_print=True,xml_declaration=True))
newfile.close()
print('trans finish')


