#!/usr/bin/python3

from time import sleep
import os,re
from debug_test import traceback_test
from autotest import ver_apk,deviceID,ver_loca


#Connectivity Constraints
@traceback_test(act=ver_apk,phone=deviceID)
def Connectivity_Constraints(autt):
	autt.close_error()
	autt.open_setting()
	autt.scoll_to_find('More').click()
	autt.scoll_to_find('Airplane Mode').click()
	autt.scoll_to_find('Airplane Mode').click()
	pattern = re.compile( r'\d+' )
	ap_state=pattern.findall(os.popen("adb -s {phone} shell settings list global |grep airplane_mode_on=".format(phone=deviceID)).read())
	if ap_state[0]=='0':
		autt.scoll_to_find('Airplane Mode').click()
	autt.close_setting()
	autt.creat_folder('Other_test')
	autt.scoll_to_find('Connectivity Constraints').click()
	autt.remove_desc()
	autt.scoll_to_find('Start test').click()
	sleep(30)
	autt.screencap(folder='Other_test',name='Connectivity_Constraints')
	autt.press_pass()


#Idle Mode Constraints
@traceback_test(act=ver_apk,phone=deviceID)
def Idle_Mode_Constraints(autt):
	os.system("adb -s {phone} shell svc power stayon true".format(phone=autt.phone))#stay awake
	autt.close_error()
	autt.scoll_to_find('Idle Mode Constraints').click()
	autt.remove_desc()
	autt.scoll_to_find('Start test').click()
	sleep(30)
	autt.scoll_to_find('Switch off screen and wait for it to turn on to continue.')
	autt.presskeyevent('KEYCODE_POWER')
	sleep(5)
	autt.move_unlock(130)
	sleep(2)
	autt.screencap(folder='Other_test',name='Idle_Mode_Constraints')
	autt.press_pass()
	os.system("adb -s {phone} shell svc power stayon false".format(phone=deviceID))




#Car Dock Test (maybe error?)
@traceback_test(act=ver_apk,phone=deviceID)
def Car_Dock_Test(autt):
	autt.close_error()
	now_act=autt.getact()
	autt.scoll_to_find('Car Dock Test').click()
	autt.remove_desc()
	autt.dr.find_element_by_name('Enable Car Mode').click()
	sleep(1)
	try:
		autt.dr.find_element_by_class_name('android.widget.FrameLayout')
		autt.dr.find_element_by_name('CTS Verifier').click()
		autt.dr.find_element_by_name('Always').click()
		sleep(1)
		autt.presskeyevent('KEYCODE_HOME')
	except Exception:
		raise Exception('Car Dock Test error')
	
	finally:  #reset permission
		autt.open_setting()
		autt.scoll_to_find('Apps').click()
		autt.scoll_to_find('Reset apps').click()
		autt.scoll_to_find('Reset apps').click()
		sleep(2)
		autt.close_setting()
		os.system("adb -s {phone} shell am start -S {act} > /dev/null".format(phone=autt.phone,act=now_act))
		autt.allow_permission()







#Data Backup Test
@traceback_test(act=ver_apk,phone=deviceID)
def Data_Backup_Test(autt):
	autt.close_error()
	now_act=autt.getact()
	autt.scoll_to_find('Data Backup Test').click()
	autt.remove_desc()
	autt.creat_folder('Other_test')
	autt.scoll_to_find('Generate Test Data').click()
	autt.remove_desc() #creat date
	result=autt.dr.find_elements_by_class_name('android.widget.TextView')[-1].get_attribute('text')
	autt.screencap(folder='Other_test',name='Data_Backup_Test0')
	os.system("adb -s {phone} shell bmgr enable true".format(phone=autt.phone))
	sleep(2)
	os.system("adb -s {phone} shell bmgr transport android/com.android.internal.backup.LocalTransport".format(phone=autt.phone))
	sleep(2)
	os.system("adb -s {phone} shell bmgr run".format(phone=autt.phone))
	sleep(2)
	os.system("adb -s {phone} uninstall com.android.cts.verifier".format(phone=autt.phone))
	sleep(2)
	os.system("adb -s {phone} install -rg '{ver_loca}'".format(phone=autt.phone,ver_loca=ver_loca))
	sleep(2)
	os.system("adb -s {phone} shell am start -S {act}".format(phone=autt.phone,act=now_act))
	autt.allow_permission()
	autt.scoll_to_find('Data Backup Test').click()
	autt.remove_desc()
	autt.screencap(folder='Other_test',name='Data_Backup_Test1')
	if result==autt.dr.find_elements_by_class_name('android.widget.TextView')[-1].get_attribute('text'):
		autt.press_pass()
	else:
		autt.press_fail()



#Notification Listener Test
@traceback_test(act=ver_apk,phone=deviceID)
def Notification_Listener_Test(autt):
	autt.close_error()
	autt.scoll_to_find('Notification Listener Test').click()
	autt.remove_desc()
	sleep(1)
	to_lis=autt.dr.find_elements_by_name('Launch Settings')
	if to_lis[0].get_attribute('clickable')=='true':
		to_lis[0].click()
		autt.scoll_to_find('Notification Listener for CTS Verifier').click()
		sleep(1)
		autt.scoll_to_find('Allow').click()
		autt.presskeyevent('KEYCODE_BACK')
	for i in range(5):
		autt.move_up(220)
	sleep(40)
	tf_lis=autt.dr.find_elements_by_name('Launch Settings')
	if tf_lis[-1].get_attribute('clickable')=='true':
		tf_lis[-1].click()
		autt.scoll_to_find('Notification Listener for CTS Verifier').click()
		sleep(1)
		autt.presskeyevent('KEYCODE_BACK')
	sleep(30)
	autt.press_pass()


#Notification Package Priority Test
@traceback_test(act=ver_apk,phone=deviceID)
def Notification_Package_Priority_Test(autt):
	autt.close_error()
	autt.scoll_to_find('Notification Package Priority Test').click()
	autt.remove_desc()
	sleep(1)
	ls=autt.dr.find_element_by_name('Launch Settings')
	if ls.get_attribute('clickable')=='true':
		ls.click()
		autt.scoll_to_find('Notification Listener for CTS Verifier').click()
		sleep(1)
		autt.scoll_to_find('Allow').click()
		autt.presskeyevent('KEYCODE_BACK')
	for i in range(5):
		autt.move_up(220)
	sleep(40)
	print('sleep end')
	imd=autt.dr.find_elements_by_name("I'm done")
	if imd[0].get_attribute('clickable')=='true':
		imd[0].click()
		sleep(30)
	if imd[1].get_attribute('clickable')=='true':
		autt.open_setting()
		autt.scoll_to_find('Notification and Control Center').click()
		autt.scoll_to_find('Notice Management').click()
		sleep(5)
		autt.scoll_to_find('CTS Verifier').click()
		autt.scoll_to_find('Enable for important notifications').click()
		autt.close_setting()
		imd[1].click()
		sleep(30)
		autt.press_pass()
		autt.open_setting()
		autt.scoll_to_find('Notification and Control Center').click()
		autt.scoll_to_find('Notice Management').click()
		sleep(5)
		autt.scoll_to_find('CTS Verifier').click()
		autt.scoll_to_find('Enable for important notifications').click()
		autt.close_setting()


''' #no good network!
#Streaming Video Quality Verifier
@traceback_test(act=ver_apk,phone=deviceID)
def Streaming_Video_Quality_Verifier(autt):
	autt.close_error()
	autt.scoll_to_find('Streaming Video Quality Verifier').click()
	autt.remove_desc()
'''
