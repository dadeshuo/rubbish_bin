#!/usr/bin/python3
import re,os
from time import sleep

deviceID="459DQ4C6MVIJMBV4"
def sys_set_input(phone):
	out = os.popen("adb -s {phone} shell settings get secure enabled_input_methods"
		.format(phone=phone)).read().replace('\n','')
	pattern1 = re.compile( r";.*")
	all_input=[pattern1.sub('',item) for item in out.split(':')]
	latin_input=list(filter(lambda item: 'latin' in item ,all_input))[0]
	os.system("adb -s {phone} shell settings put secure enabled_input_methods NULL"
		.format(phone=phone))
	os.system("adb -s {phone} shell settings put secure enabled_input_methods {latin_input}"
		.format(phone=phone,latin_input=latin_input))
	os.system("adb  -s {phone} shell settings put secure default_input_method {latin_input}"
		.format(phone=phone,latin_input=latin_input))

if __name__=='__main__':
	
	sys_set_input(deviceID)
