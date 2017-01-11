#!/usr/bin/python3

from time import sleep
import os
import re
from debug_test import traceback_test
from autotest import ver_apk,deviceID
from functools import wraps


def pre_Sensor(autt):
	os.system("adb -s {phone} shell svc power stayon false".format(phone=deviceID))#stay awake

	autt.close_error()
	autt.open_setting()
	autt.scoll_to_find('Advanced Settings').click()
	autt.scoll_to_find('Location').click()
	if autt.scoll_to_find('Mode').is_enabled():
		autt.dr.find_elements_by_class_name('android.widget.Switch')[0].click()
	autt.close_setting()

	autt.open_setting()
	autt.scoll_to_find('More').click()
	autt.scoll_to_find('Airplane Mode').click()
	autt.scoll_to_find('Airplane Mode').click()
	pattern = re.compile( r'\d+' )
	ap_state=pattern.findall(os.popen("adb -s {phone} shell settings list global |grep airplane_mode_on=".format(phone=deviceID)).read())
	if ap_state[0]=='0':
		autt.scoll_to_find('Airplane Mode').click()
	autt.close_setting()

		
	ro_state=pattern.findall(os.popen("adb -s {phone} shell settings list system |grep accelerometer_rotation=".format(phone=deviceID)).read())
	if ro_state[0]=='1':
		autt.open_setting()
		autt.scoll_to_find('Display').click()
		autt.scoll_to_find('Auto-rotate screen').click()
		autt.close_setting()

	ab_state=pattern.findall(os.popen("adb -s {phone} shell settings list system |grep screen_brightness_mode=".format(phone=deviceID)).read())#adaptive brightness
	if ab_state[0]=='1':
		autt.open_setting()
		autt.scoll_to_find('Display').click()
		autt.scoll_to_find('Adaptive brightness').click()
		autt.close_setting()
	
	autt.open_setting()
	autt.scoll_to_find('Security').click()
	autt.scoll_to_find('Device Administrators').click()
	autt.scoll_to_find('Sensor Tests Device Admin Receiver').click()
	elelist=autt.get_all_elewant('amigo.widget.AmigoButton','text')
	if 'Deactivate' in elelist:
		pass
	elif 'Activate' in elelist:
		elelist['Activate'].click()
	else:
		raise Exception("CTS ver can't find ")
	autt.close_setting()



#CTS Sensor Batching Tests
@traceback_test(act=ver_apk,phone=deviceID)
def CTS_Sensor_Batching_Tests(autt):
	autt.close_error()
	pre_Sensor(autt)
	autt.scoll_to_find('CTS Sensor Batching Tests').click()
	autt.remove_desc()
	autt.scoll_to_find('Next').click()
	autt.scoll_to_find('Next').click()
	sleep(1)
	autt.presskeyevent('KEYCODE_POWER')
	sleep(0.5)
	autt.move_unlock(130)
	try:
		for i in range(300):
			sleep(10)
			for ele in autt.dr.find_elements_by_class_name('android.widget.Button'):
				if 'ass' in ele.get_attribute('text'):
					print(ele.get_attribute('text'))
					ele.click()
					raise Exception
			
	except Exception:
		pass


#CTS Sensor Integration Tests
@traceback_test(act=ver_apk,phone=deviceID)
def CTS_Sensor_Integration_Tests(autt):
	autt.close_error()
	pre_Sensor(autt)
	autt.scoll_to_find('CTS Sensor Integration Tests').click()
	autt.remove_desc()
	autt.scoll_to_find('Next').click()
	autt.scoll_to_find('Next').click()
	sleep(1)
	autt.presskeyevent('KEYCODE_POWER')
	sleep(0.5)
	autt.move_unlock(130)
	try:
		for i in range(300):
			sleep(10)
			for ele in autt.dr.find_elements_by_class_name('android.widget.Button'):
				if 'ass' in ele.get_attribute('text'):
					print(ele.get_attribute('text'))
					ele.click()
					raise Exception
			
	except Exception:
		pass

	


#CTS Sensor Test
@traceback_test(act=ver_apk,phone=deviceID)
def CTS_Sensor_Test(autt):
	autt.close_error()
	pre_Sensor(autt)
	autt.scoll_to_find('CTS Sensor Test').click()
	autt.remove_desc()
	autt.scoll_to_find('Next').click()
	autt.scoll_to_find('Next').click()
	sleep(1)
	autt.presskeyevent('KEYCODE_POWER')
	sleep(0.5)
	autt.move_unlock(130)
	try:
		for i in range(300):
			sleep(10)
			for ele in autt.dr.find_elements_by_class_name('android.widget.Button'):
				if 'ass' in ele.get_attribute('text'):
					print(ele.get_attribute('text'))
					ele.click()
					raise Exception
			
	except Exception:
		pass




#CTS Single Sensor Tests
@traceback_test(act=ver_apk,phone=deviceID)
def CTS_Single_Sensor_Tests(autt):
	autt.close_error()
	pre_Sensor(autt)
	autt.scoll_to_find('CTS Single Sensor Tests').click()
	autt.remove_desc()
	autt.scoll_to_find('Next').click()
	autt.scoll_to_find('Next').click()
	sleep(1)
	autt.presskeyevent('KEYCODE_POWER')
	sleep(0.5)
	autt.move_unlock(130)
	try:
		for i in range(300):
			sleep(10)
			for ele in autt.dr.find_elements_by_class_name('android.widget.Button'):
				if 'ass' in ele.get_attribute('text'):
					print(ele.get_attribute('text'))
					ele.click()
					raise Exception
			
	except Exception:
		pass



#Device Suspend Tests
@traceback_test(act=ver_apk,phone=deviceID)
def Device_Suspend_Tests(autt):
	autt.close_error()
	pre_Sensor(autt)
	autt.scoll_to_find('Device Suspend Tests').click()
	autt.remove_desc()
	autt.scoll_to_find('Next').click()
	autt.scoll_to_find('Next').click()
	try:
		for i in range(300):
			sleep(10)
			for ele in autt.dr.find_elements_by_class_name('android.widget.Button'):
				if 'ass' in ele.get_attribute('text'):
					print(ele.get_attribute('text'))
					ele.click()
					raise Exception
			
	except Exception:
		pass


#Magnetic Field Measurement Tests
@traceback_test(act=ver_apk,phone=deviceID)
def Magnetic_Field_Measurement_Tests(autt):
	autt.close_error()
	pre_Sensor(autt)
	autt.scoll_to_find('Magnetic Field Measurement Tests').click()
	autt.remove_desc()
	autt.scoll_to_find('Next').click()
	autt.scoll_to_find('Next').click()
	try:
		for i in range(300):
			sleep(10)
			for ele in autt.dr.find_elements_by_class_name('android.widget.Button'):
				if 'ass' in ele.get_attribute('text'):
					print(ele.get_attribute('text'))
					ele.click()
					raise Exception
			
	except Exception:
		pass

#Significant Motion Tests
@traceback_test(act=ver_apk,phone=deviceID)
def Significant_Motion_Tests(autt):
	autt.close_error()
	pre_Sensor(autt)
	autt.scoll_to_find('Significant Motion Tests').click()
	autt.remove_desc()
	autt.scoll_to_find('Next').click()
	try:
		for i in range(300):
			sleep(10)
			for ele in autt.dr.find_elements_by_class_name('android.widget.Button'):
				if 'ass' in ele.get_attribute('text'):
					print(ele.get_attribute('text'))
					ele.click()
					raise Exception
			
	except Exception:
		pass



