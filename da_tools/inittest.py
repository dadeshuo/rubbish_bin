#!/usr/bin/python3


import os,re,time
import sys
import getopt
import multiprocessing

path_other_app=r'/media/da/base'
path_cts=r'/home/da/cts'
path_new_cts=r'/home/da/new/cts'
path_media=r'/home/da/android-cts-media-1.2'
path_ver=r'/home/da/android-cts-verifier'
path_new_ver=r'/home/da/new/android-cts-verifier'
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

def sys_set_lock_and_dis(phone):
	os.system("adb -s {phone} shell svc power stayon true".format(phone=phone))#stay awake
	os.system("adb -s {phone} shell settings put system screen_brightness 70".format(phone=phone))#law screen_brightness
	os.system("adb -s {phone} shell settings put system screen_off_timeout 1800000".format(phone=phone))#30min screen_off
	

def com_op(phone):
	os.system('adb -s {name} shell am start -a android.intent.action.CALL -d tel:10010'.format(name=phone))
	time.sleep(4)
	os.system('adb -s {name} shell am start -a android.intent.action.VIEW -d http://testerhome.com'.format(name=phone))
	time.sleep(1)
	sys_set_input(phone)
	sys_set_lock_and_dis(phone)
	

def cts_l(phone,path):
	com_op(phone)
	os.system('adb -s {name} install -r "{path_other_app}/ss.apk"'.format(path_other_app=path_other_app,name=phone))
	os.system('adb -s {name} install -r "{path_cts}/5.1/android-cts/repository/testcases/CtsDeviceAdmin.apk"'.format(path_cts=path,name=phone))
	os.system('adb -s {name} shell settings put global verifier_verify_adb_installs 0'.format(name=phone))
	time.sleep(1)
	os.system("adb -s {phone} shell am start -S com.android.settings/com.android.settings.GnSettingsTabActivity".format(phone=phone))
	os.system('{path_media}/copy_media.sh all -s {name}'.format(path_media=path_media,name=phone))
	

def cts_m(phone,path):
	com_op(phone)
	os.system('adb -s {name} push {path_other_app}/openvpn /storage/sdcard0/openvpn'.format(path_other_app=path_other_app,name=phone))
	os.system('adb -s {name} install -r "{path_other_app}/openvpn.apk"'.format(path_other_app=path_other_app,name=phone))
	os.system('adb -s {name} install -r "{path_other_app}/ss.apk"'.format(path_other_app=path_other_app,name=phone))
	os.system('adb -s {name} install -r "{path_cts}/6.0/android-cts/repository/testcases/CtsDeviceAdmin.apk"'.format(path_cts=path,name=phone))
	os.system('adb -s {name} shell settings put global verifier_verify_adb_installs 0'.format(name=phone))
	time.sleep(1)
	os.system("adb -s {phone} shell am start -S com.android.settings/com.android.settings.GnSettingsTabActivity".format(phone=phone))
	os.system('{path_media}/copy_media.sh all -s {name}'.format(path_media=path_media,name=phone))

def ects_l(phone,path):
	com_op(phone)
	os.system('adb -s {name} install -r "{path_other_app}/ss.apk"'.format(path_other_app=path_other_app,name=phone))
	os.system('adb -s {name} install -r "{path_cts}/5.1/android-cts/repository/testcases/CtsDeviceAdmin.apk"'.format(path_cts=path,name=phone))
	os.system('adb -s {name} shell settings put global verifier_verify_adb_installs 0'.format(name=phone))
	time.sleep(1)
	os.system("adb -s {phone} shell am start -S com.android.settings/com.android.settings.GnSettingsTabActivity".format(phone=phone))


def ects_m(phone,path):
	com_op(phone)
	os.system('adb -s {name} push {path_other_app}/openvpn /storage/sdcard0/openvpn'.format(path_other_app=path_other_app,name=phone))
	os.system('adb -s {name} install -r "{path_other_app}/openvpn.apk"'.format(path_other_app=path_other_app,name=phone))
	os.system('adb -s {name} install -r "{path_other_app}/ss.apk"'.format(path_other_app=path_other_app,name=phone))
	os.system('adb -s {name} install -r "{path_cts}/6.0/android-cts/repository/testcases/CtsDeviceAdmin.apk"'.format(path_cts=path,name=phone))
	os.system('adb -s {name} shell settings put global verifier_verify_adb_installs 0'.format(name=phone))
	time.sleep(1)
	os.system("adb -s {phone} shell am start -S com.android.settings/com.android.settings.GnSettingsTabActivity".format(phone=phone))


def gts(phone):
	com_op(phone)
	os.system('adb -s {name} install -r "{path_other_app}/ss.apk"'.format(path_other_app=path_other_app,name=phone))

def ver(phone,vision,ver_path):
	sys_set_input(phone)
	#os.system("adb -s {phone} shell svc power stayon true".format(phone=phone))#stay awake
	os.system("adb -s {phone} shell settings put system screen_brightness 150".format(phone=phone))#law screen_brightness
	os.system("adb -s {phone} shell settings put system screen_off_timeout 1800000".format(phone=phone))#30min screen_off
	path={'Lollipop':'5.1','Marshmallow':'6.0'}.get(vision)
	lis=[]
	for root, dirs, files in os.walk(ver_path+'/'+path+'/'):
		for name in files:
			lis.append(os.path.join(root, name))
	pattern = re.compile(r'^.*apk$')
	for item in list(filter(lambda x:pattern.findall(x)!=[],lis)):
		os.system('adb -s {name} install -rg "{item}"'.format(name=phone,item=item))
	os.system('adb -s {name} install -rg "{path_other_app}/ss.apk"'.format(path_other_app=path_other_app,name=phone)) 
	os.system("adb -s {phone} uninstall com.commsource.beautyplus".format(phone=phone))
	#os.system("adb -s {phone} shell am start -a  android.media.action.STILL_IMAGE_CAMERA".format(phone=phone))
def checklist(lis,phone_id_all):
	try:
		opts, args = getopt.getopt(lis[1:], "s:o,p:o,v:o")
	except getopt.GetoptError as err:
		# print help information and exit:
		print(err) 
		sys.exit(2)
	phone_id=phone_id_all
	plan='cts'
	vision='Lollipop'
	plan_all={'cts':'cts','gts':'gts','xts':'gts','ver':'ver','ects':'ects','ncts':'ncts','nects':'nects','nver':'nver'}
	vision_all={'5':'Lollipop','6':'Marshmallow'}
	for o, a in opts:
		if a =='':
			continue
		elif o == "-s" and a in phone_id_all:
			phone_id=[a]
		elif o == "-p":
			plan=plan_all.get(a,'cts')
		elif o == "-v":
			vision =vision_all.get(a,'Lollipop')
		else:
			assert False, "unhandled option"
	return [phone_id,plan,vision]

def getphone():
	out = os.popen("adb devices|grep '\<device\>'").read()
	test=out.split('\n')
	phone_id_all=[]
	for item in test[:-1]:
		phone_id_all.append(item.split( '\t')[0])
	return phone_id_all

def init_test(phone,plan,vision):
		if plan=='cts':
			if vision=='Lollipop':
				cts_l(phone,path_cts)
			elif vision=='Marshmallow':
				cts_m(phone,path_cts)
			else:
				assert False, "unknow vision"
		elif plan=='gts':
			gts(phone)
		elif plan=='ver':
			ver(phone,vision,path_ver)
		elif plan=='nver':
			ver(phone,vision,path_new_ver)
		elif plan=='ects':
			if vision=='Lollipop':
				ects_l(phone,path_cts)
			elif vision=='Marshmallow':
				ects_m(phone,path_cts)
			else:
				assert False, "unknow vision"
		elif plan=='ncts':
			if vision=='Lollipop':
				cts_l(phone,path_new_cts)
			elif vision=='Marshmallow':
				cts_m(phone,path_new_cts)
			else:
				assert False, "unknow vision"
		elif plan=='nects':
			if vision=='Lollipop':
				ects_l(phone,path_new_cts)
			elif vision=='Marshmallow':
				ects_m(phone,path_new_cts)
			else:
				assert False, "unknow vision"
		else:
			assert False, "unknow plan"

if __name__=='__main__':
	phone_id_all=getphone()
	if phone_id_all != []:
		item=checklist(sys.argv,phone_id_all)
		process_list=[]
		for phone in item[0]:
			temp=multiprocessing.Process(target=init_test, args=(phone,item[1], item[2]))
			process_list.append(temp)
			temp.start()
			
		for item in process_list:
			item.join()

	print('all finish')


