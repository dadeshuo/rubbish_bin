#!/usr/bin/python3


from lxml import etree
import time,os,sys
import getopt

def getroad(root,pos=''):
	for child in root:
		if child.tag == 'TestSuite':
			getroad(child,pos+child.get('name')+'.')
		else:
			for item in child:
				if item.tag == 'Test' and item.get('result')!='notExecuted':
					item.set('result','notExecuted')


			
class xmlbody():
	def __init__(self,org,enable):
		self.org=org
		self.enable=enable
		self.tree = etree.parse(org)
		self.path=os.path.abspath(os.path.dirname(org))
		with open(self.org,mode='rb') as read_title:
			self.first=read_title.readline()

	def changexml(self):
		root = self.tree.getroot()
		for child in root:
			if child.tag == 'TestPackage' and child.get('appPackageName')==self.enable:
				getroad(child,'')
		f=open(self.org+'.enable.xml','wb')
		f.write(etree.tostring(self.tree,encoding= "UTF-8",pretty_print=True,xml_declaration=True))
		f.close()

if __name__=='__main__':
  
	try:
		opts,args= getopt.getopt(sys.argv[1:], "e:o,f:o")
	except getopt.GetoptError as err:
	# print help information and exit:
		print(err) 
		sys.exit(2)

	for o, a in opts:
		if o =='':
			continue
		elif o == "-f":
			org=a

		elif o == "-e":
			enable=a

		else:
			assert False, "unhandled option"
	test=xmlbody(org,enable)
	test.changexml()



