#!/usr/bin/python3

from time import sleep
import os
from debug_test import traceback_test
from autotest import ver_apk,deviceID

#SUID File Scanner
@traceback_test(act=ver_apk,phone=deviceID)
def SUID_File_Scanner(autt):
	autt.close_error()
	autt.scoll_to_find('SUID File Scanner').click()
	autt.remove_desc()
	try:
		for i in range(300):
			sleep(10)
			if  len(autt.dr.find_elements_by_name('OK'))==1:
				autt.dr.find_elements_by_name('OK')[0].click()
				autt.press_pass()
				raise Exception
			
	except Exception:
		pass
	


#Security 
@traceback_test(act=ver_apk,phone=deviceID)
def Security(autt):
	autt.close_error()

	autt.open_setting()
	autt.scoll_to_find('Security').click()
	autt.scoll_to_find('Device Administrators').click()
	autt.scoll_to_find('CTS Verifier').click()
	elelist=autt.get_all_elewant('amigo.widget.AmigoButton','text')
	if 'Activate' in elelist:
		pass
	elif 'Deactivate' in elelist:
		elelist['Deactivate'].click()
	else:
		raise Exception("CTS ver can't find ")
	autt.close_setting()

	autt.scoll_to_find('Keyguard Password Verification').click()
	autt.remove_desc()
	autt.scoll_to_find('Set password').click()
	autt.scoll_to_find('Mixed password').click()
	autt.scoll_to_find('No thanks').click()
	autt.scoll_to_find('Continue').click()
	sleep(5)
	autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'testpassword')
	sleep(1)
	autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'\n')
	sleep(5)
	autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'testpassword')
	sleep(5)
	autt.scoll_to_find('OK').click()
	sleep(2)
	autt.presskeyevent('KEYCODE_BACK')
	#KeyChain Storage Test
	autt.presskeyevent('KEYCODE_BACK')
	autt.scoll_to_find('KeyChain Storage Test').click()
	autt.remove_desc()
	autt.scoll_to_find('Next').click()
	sleep(0.5)
	autt.scoll_to_find('Next').click()
	sleep(0.5)
	autt.scoll_to_find('Next').click()
	sleep(0.5)
	autt.scoll_to_find('OK').click()
	sleep(0.5)
	autt.scoll_to_find('OK').click()
	sleep(0.5)
	autt.scoll_to_find('Next').click()
	sleep(0.5)
	autt.scoll_to_find('Next').click()
	sleep(1)
	autt.scoll_to_find('Allow').click()
	sleep(0.5)
	autt.press_pass()
	#Lock Bound Keys Test
	autt.scoll_to_find('Lock Bound Keys Test').click()
	autt.remove_desc()
	autt.scoll_to_find('Start Test').click()
	sleep(10)
	autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'testpassword')
	sleep(1)
	autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'\n')
	sleep(2)
	autt.press_pass()
	
	autt.scoll_to_find('Keyguard Password Verification').click()
	autt.remove_desc()
	autt.scoll_to_find('Change password').click()
	sleep(1)
	autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'testpassword')
	sleep(1)
	autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'\n')
	autt.scoll_to_find('Swipe').click()
	autt.scoll_to_find('Yes, remove').click()

	autt.press_pass()
