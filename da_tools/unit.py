#!/usr/bin/python3


import os
import multiprocessing
import sys,re
path_media=r'/home/da/android-cts-media-1.2'
def cyfile(phone):
	os.system('{path_media}/copy_media.sh all -s {name}'.format(path_media=path_media,name=phone))

phonelist=[]
process_list=[]
out = os.popen("adb devices|grep '\<device\>'").read()
test=out.split('\n')
for item in test[:-1]:
	phonelist.append(item.split( '\t')[0])
for phone in phonelist:
	temp=multiprocessing.Process(target=cyfile, args=(phone,))
	process_list.append(temp)
	temp.start()
			
for item in process_list:
	item.join()

