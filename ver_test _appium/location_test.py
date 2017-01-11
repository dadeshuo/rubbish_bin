#!/usr/bin/python3

from time import sleep
import os
from debug_test import traceback_test
from autotest import ver_apk,deviceID


#Battery Saving Mode Test
@traceback_test(act=ver_apk,phone=deviceID)
def Battery_Saving_Mode_Test(autt):
	autt.close_error()
	autt.open_setting()
	autt.scoll_to_find('Advanced Settings').click()
	autt.scoll_to_find('Location').click()
	if not autt.scoll_to_find('Mode').is_enabled():
		autt.dr.find_elements_by_class_name('android.widget.Switch')[0].click()
	autt.scoll_to_find('Mode').click()
	autt.scoll_to_find('Battery saving').click()
	autt.close_setting()
	
	autt.scoll_to_find('Battery Saving Mode Test').click()
	autt.remove_desc()
	sleep(5)
	autt.press_pass()


#Device Only Mode Test
@traceback_test(act=ver_apk,phone=deviceID)
def Device_Only_Mode_Test(autt):
	autt.close_error()
	autt.open_setting()
	autt.scoll_to_find('Advanced Settings').click()
	autt.scoll_to_find('Location').click()
	if not autt.scoll_to_find('Mode').is_enabled():
		autt.dr.find_elements_by_class_name('android.widget.Switch')[0].click()
	autt.scoll_to_find('Mode').click()
	autt.scoll_to_find('Device only').click()
	autt.close_setting()
	
	autt.scoll_to_find('Device Only Mode Test').click()
	autt.remove_desc()
	sleep(5)
	autt.press_pass()


#High Accuracy Mode Test
@traceback_test(act=ver_apk,phone=deviceID)
def High_Accuracy_Mode_Test(autt):
	autt.close_error()
	autt.open_setting()
	autt.scoll_to_find('Advanced Settings').click()
	autt.scoll_to_find('Location').click()
	if not autt.scoll_to_find('Mode').is_enabled():
		autt.dr.find_elements_by_class_name('android.widget.Switch')[0].click()
	autt.scoll_to_find('Mode').click()
	autt.scoll_to_find('High accuracy').click()
	autt.close_setting()
	
	autt.scoll_to_find('High Accuracy Mode Test').click()
	autt.remove_desc()
	sleep(5)
	autt.press_pass()


#Location Mode Off Test
@traceback_test(act=ver_apk,phone=deviceID)
def Location_Mode_Off_Test(autt):
	autt.close_error()
	autt.open_setting()
	autt.scoll_to_find('Advanced Settings').click()
	autt.scoll_to_find('Location').click()
	if autt.scoll_to_find('Mode').is_enabled():
		autt.dr.find_elements_by_class_name('android.widget.Switch')[0].click()
	autt.close_setting()
	
	autt.scoll_to_find('Location Mode Off Test').click()
	autt.remove_desc()
	sleep(5)
	autt.press_pass()



