#!/usr/bin/python3

from appium import webdriver
from time import sleep
import os
import autotest
from debug_test import traceback_test
from camera_test import *
from BYOD_test import * 
from Device_Administration_test import * 
from location_test import *
from Sensors_test import *
from Security_test import *
from Projection_test import *
from Other_test import *

deviceID=autotest.deviceID
ver_apk='com.android.cts.verifier/com.android.cts.verifier.CtsVerifierActivity'
ver_loca='/home/da/new/android-cts-verifier/6.0/CtsVerifier.apk'
############################  
 
desired_caps = {}
desired_caps['deviceName'] = deviceID
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
desired_caps['appPackage'] = 'com.android.cts.verifier'
desired_caps['appActivity'] = '.CtsVerifierActivity'
desired_caps["noReset"]="true"
desired_caps['udid']= deviceID



if __name__=='__main__':
	dr = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
	autt=autotest.auto_test(dr,deviceID)
	
	Data_Backup_Test(autt)
	
	Camera_Formats(autt)
	
	Camera_ITS_Test(autt)

	Camera_Intents(autt)

	Camera_Orientation(autt)
	
	Camera_Video(autt)
	
	Battery_Saving_Mode_Test(autt)
	Device_Only_Mode_Test(autt)
	High_Accuracy_Mode_Test(autt)
	Location_Mode_Off_Test(autt)
	
	#CTS_Sensor_Batching_Tests(autt)
	#CTS_Sensor_Integration_Tests(autt)
	
	#CTS_Sensor_Test(autt)
	#CTS_Single_Sensor_Tests(autt)
	
	#Device_Suspend_Tests(autt)
	
	#Magnetic_Field_Measurement_Tests(autt)
	
	#Significant_Motion_Tests(autt) #maybe fail in some project
	
	Projection_Scrolling_List_Test(autt)

	Projection_Offscreen_Activity(autt)

	Projection_Widget_Test(autt)
	Notification_Listener_Test(autt)
	Notification_Package_Priority_Test(autt)
	
	BYOD_Managed_Provisioning(autt)
	
	Connectivity_Constraints(autt)
	
	Idle_Mode_Constraints(autt)
	
	Device_Owner_Provisioning(autt)
	
	SUID_File_Scanner(autt)
	
	Security(autt)
	
	Keyguard_Disabled_Features_Test(autt) 
	
	Redacted_Notifications_Keyguard_Disabled_Features_Test(autt)
	
	Screen_Lock_Test(autt)
	
	
	Device_Owner_Tests(autt)

	Car_Dock_Test(autt)
	
	#autotest.sys_set_input(deviceID)
	dr.quit


'''
find_ele.scoll_to_find(dr,'BYOD Managed Provisioning',phone_move).click()

find_ele.scoll_to_find(dr,'Start BYOD provisioning flow',phone_move).click()
find_ele.scoll_to_find(dr,'Set up',phone_move).click()
find_ele.scoll_to_find(dr,'OK',phone_move).click()
sleep(6)
find_ele.scoll_to_find(Profile owner installed).click()



Launcher_apk='com.gionee.amisystem'
os.system('adb -s {phone} shell pm clear {Launcher_apk}'.format(phone=desired_caps['deviceName'],Launcher_apk=Launcher_apk)) 



find_ele.scoll_to_find(dr,'Work notification is badged',phone_move).click()
find_ele.scoll_to_find(dr,'Go',phone_move).click()
phone_move.move_notice()
os.system('adb -s {phone} shell screencap -p /sdcard/Work_notification_is_badged.png').format(phone=desired_caps['deviceName']))
os.system('adb -s {phone} shell input keyevent KEYCODE_BACK').format(phone=desired_caps['deviceName']))
find_ele.scoll_to_find(dr,'Pass',phone_move).click()


find_ele.scoll_to_find(dr,'Work status icon is displayed',phone_move).click()
find_ele.scoll_to_find(dr,'Go',phone_move).click()
Pass

##############################



os.system('adb shell input keyevent KEYCODE_POWER')
sleep(2)
os.system('adb shell input keyevent KEYCODE_POWER')
sleep(1)
m.move_up()
dr.find_element_by_class_name('android.widget.EditText').send_keys(u'testpassword\n')
dr.quit


try:
	print(find_ele.set_device_adm(desired_caps['deviceName'],dr,m))

finally: 
	print('quit')
	dr.quit
#dr.implicitly_wait(5)


getelement(dr.find_elements_by_id('com.tencent.mm:id/cb'),'name','huangwei').click()
dr.implicitly_wait(5)
dr.find_element_by_class_name('android.widget.EditText').send_keys(u'lol')
dr.find_element_by_name('发送').click()
dr.find_element_by_class_name('android.widget.EditText').send_keys(u'这句话是靠程序敲出来的,哈哈，hello appium')
dr.find_element_by_name('发送').click()
getelement(dr.find_elements_by_class_name('android.widget.ImageButton'),'name','表情').click()
getelement(dr.find_elements_by_class_name('android.widget.ImageButton'),'name','自定义表情').click()
dr.find_elements_by_class_name('com.tencent.mm.ui.MMImageView')[6].click()


dr.implicitly_wait(5)
dr.send_keys('test')
'''

