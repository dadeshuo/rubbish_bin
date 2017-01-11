#!/usr/bin/python3


import os
import multiprocessing
import sys,re
def cyfile(name):
	os.system('adb -s {name} pull /sdcard/ctsVerifierReports /media/da/base/ver'.format(name=phone))

phonelist=[]
process_list=[]
out = os.popen("adb devices|grep '\<device\>'").read()
test=out.split('\n')
for item in test[:-1]:
	phonelist.append(item.split( '\t')[0])
for phone in phonelist:
	print(phone)
	temp=multiprocessing.Process(target=cyfile, args=(phone,))
	process_list.append(temp)
	temp.start()
			
for item in process_list:
	item.join()

