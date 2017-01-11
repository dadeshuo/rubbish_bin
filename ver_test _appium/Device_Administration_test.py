#!/usr/bin/python3

from time import sleep
import os
from debug_test import traceback_test
from autotest import ver_apk,deviceID


#Keyguard Disabled Features Test
@traceback_test(act=ver_apk,phone=deviceID)
def Keyguard_Disabled_Features_Test(autt):
	autt.close_error()
	os.system("adb -s {phone} shell svc power stayon true".format(phone=autt.phone))#stay awake
	autt.scoll_to_find('Keyguard Disabled Features Test').click()
	autt.creat_folder('Keyguard_Disabled_Features_Test')
	autt.remove_desc()
	'''	
	autt.open_setting()
	autt.scoll_to_find('Security').click()
	autt.scoll_to_find('Screen Lock').click()
	autt.scoll_to_find('Security password').click()
	autt.scoll_to_find('No thanks').click()
	autt.scoll_to_find('Continue').click()

	autt.scoll_to_find('Set password').click()
	autt.scoll_to_find('Mixed password').click()
	autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'testpassword\n')
	autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'testpassword\n')

	autt.close_setting()
	'''
	autt.open_setting()
	autt.scoll_to_find('Notification and Control Center').click()
	autt.scoll_to_find('Notifications in lockscreen').click()
	autt.scoll_to_find('Prompt all new information and hide the contents').click()
	autt.close_setting()

	autt.open_setting()
	autt.scoll_to_find('Security').click()
	autt.scoll_to_find('Device Administrators').click()
	autt.scoll_to_find('CTS Verifier').click()
	elelist=autt.get_all_elewant('amigo.widget.AmigoButton','text')
	if 'Deactivate' in elelist:
		pass
	elif 'Activate' in elelist:
		elelist['Activate'].click()
	else:
		raise Exception("CTS ver can't find ")
	autt.close_setting()

	autt.scoll_to_find('Prepare test').click()
	admin_act=autt.getact()

	#Disable trust agents
	@traceback_test(act=admin_act,phone=deviceID)
	def Disable_trust_agents(autt):
		autt.close_error()
		autt.scoll_to_find('Disable trust agents').click()
		autt.scoll_to_find('Go').click()
		autt.scoll_to_find('Trust agents').click()
		if not autt.dr.find_elements_by_class_name('android.widget.Switch')[0].is_enabled():
			autt.screencap(folder='Keyguard_Disabled_Features_Test',name='Disable_trust_agents')
			autt.presskeyevent('KEYCODE_BACK')
			autt.presskeyevent('KEYCODE_BACK')
			autt.scoll_to_find('Pass').click()
		else:
			raise Exception('Disable trust agents fail')

		

	#Disable camera
	@traceback_test(act=admin_act,phone=deviceID)
	def Disable_camera(autt):
		autt.close_error()
		autt.scoll_to_find('Disable camera').click()
		autt.scoll_to_find('Go').click()
		sleep(3)
		autt.presskeyevent('KEYCODE_POWER')
		sleep(1)
		try:
			cam_icon=autt.dr.find_element_by_id('com.amigo.keyguard:id/iv_affordance_camera')
			cam_icon_x=cam_icon.location.get('x')
			cam_icon_y=cam_icon.location.get('y')
			cam_icon_h=cam_icon.size.get('height')
			cam_icon_w=cam_icon.size.get('width')
			autt.move(autt.phone,cam_icon_x+0.5*cam_icon_w,cam_icon_y+0.5*cam_icon_h,autt.cen_x,autt.cen_y,150)
		except Exception:
			autt.screencap(folder='Keyguard_Disabled_Features_Test',name='Disable_camera_no_camera')
			autt.move_unlock(130)
		sleep(0.5)
		autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'testpassword')
		sleep(1)
		autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'\n')
		sleep(2)
		autt.screencap(folder='Keyguard_Disabled_Features_Test',name='Disable_camera')
		if 'camera' in autt.getact().split('/')[0]:
			os.system("adb -s {phone} shell am force-stop {pac}".format(phone=autt.phone,pac=autt.getact().split('/')[0]))
		autt.scoll_to_find('Pass').click()


	#Disable notifications
	@traceback_test(act=admin_act,phone=deviceID)
	def Disable_notifications(autt):
		autt.close_error()
		autt.scoll_to_find('Disable notifications').click()
		autt.scoll_to_find('Go').click()
		sleep(1)
		autt.presskeyevent('KEYCODE_POWER')
		sleep(0.5)
		autt.screencap(folder='Keyguard_Disabled_Features_Test',name='Disable_notifications')
		autt.move_unlock(130)
		autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'testpassword')
		sleep(1)
		autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'\n')
		sleep(1)
		autt.scoll_to_find('Pass').click()
		
	Disable_trust_agents(autt)			
	Disable_camera(autt)
	Disable_notifications(autt)
	autt.presskeyevent('KEYCODE_BACK')
	os.system("adb -s {phone} shell svc power stayon false".format(phone=autt.phone))#stay awake

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


''' can't support reboot!

#Policy Serialization Test
@traceback_test(act=ver_apk,phone=deviceID)
def Policy_Serialization_Test(autt):
	autt.close_error()
	os.system("adb -s {phone} shell svc power stayon true".format(phone=autt.phone))#stay awake
	
	autt.open_setting()
	autt.scoll_to_find('Security').click()
	autt.scoll_to_find('Device Administrators').click()
	autt.scoll_to_find('CTS Verifier').click()
	elelist=autt.get_all_elewant('amigo.widget.AmigoButton','text')
	if 'Deactivate' in elelist:
		pass
	elif 'Activate' in elelist:
		elelist['Activate'].click()
	else:
		raise Exception("CTS ver can't find ")
	autt.close_setting()

	autt.scoll_to_find('Policy Serialization Test').click()
	autt.remove_desc()
	autt.scoll_to_find('Generate Policy').click()
	autt.scoll_to_find('Apply Policy').click()
	autt.remove_desc()
	ps_act=autt.getact()
	os.system("adb -s {phone} shell reboot".format(phone=autt.phone))#stay awake
	for i in range(300):
		out = os.popen( "adb devices|grep {phone}".format(phone=autt.phone) ).read()
		if out:
			break
		sleep(10)
	autt.move_unlock()
	os.system("adb -s {phone} shell am start -S {act}".format(phone=autt.phone,act=ps_act))
	autt.press_pass()

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
	os.system("adb -s {phone} shell svc power stayon false".format(phone=autt.phone))
'''

#Redacted Notifications Keyguard Disabled Features Test
@traceback_test(act=ver_apk,phone=deviceID)
def Redacted_Notifications_Keyguard_Disabled_Features_Test(autt):
	autt.close_error()
	os.system("adb -s {phone} shell svc power stayon true".format(phone=autt.phone))#stay awake
	autt.creat_folder('Redacted_Notifications_Keyguard_Disabled_Features_Test')
	autt.open_setting()
	autt.scoll_to_find('Security').click()
	autt.scoll_to_find('Device Administrators').click()
	autt.scoll_to_find('CTS Verifier').click()
	elelist=autt.get_all_elewant('amigo.widget.AmigoButton','text')
	if 'Deactivate' in elelist:
		pass
	elif 'Activate' in elelist:
		elelist['Activate'].click()
	else:
		raise Exception("CTS ver can't find ")
	autt.close_setting()

	autt.scoll_to_find('Redacted Notifications Keyguard Disabled Features Test').click()
	autt.remove_desc()
	autt.scoll_to_find('Prepare test').click()
	autt.scoll_to_find('Disable unredacted notifications').click()
	autt.scoll_to_find('Go').click()
	sleep(1)
	autt.presskeyevent('KEYCODE_POWER')
	sleep(1)
	autt.screencap(folder='Redacted_Notifications_Keyguard_Disabled_Features_Test',name='Redacted_Notifications_Keyguard_Disabled_Features_Test')
	
	autt.move_unlock(130)
	sleep(0.5)
	autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'testpassword') #fuck you google!
	sleep(1)
	autt.dr.find_element_by_class_name('android.widget.EditText').send_keys(u'\n')
	autt.scoll_to_find('Pass').click()
	autt.press_pass()

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
	os.system("adb -s {phone} shell svc power stayon false".format(phone=autt.phone))

#Screen Lock Test
@traceback_test(act=ver_apk,phone=deviceID)
def Screen_Lock_Test(autt):
	os.system("adb -s {phone} shell svc power stayon true".format(phone=autt.phone))
	autt.close_error()
	
	autt.open_setting()
	autt.scoll_to_find('Security').click()
	autt.scoll_to_find('Device Administrators').click()
	autt.scoll_to_find('CTS Verifier').click()
	elelist=autt.get_all_elewant('amigo.widget.AmigoButton','text')
	if 'Deactivate' in elelist:
		pass
	elif 'Activate' in elelist:
		elelist['Activate'].click()
	else:
		raise Exception("CTS ver can't find ")
	autt.close_setting()

	autt.scoll_to_find('Screen Lock Test').click()
	autt.remove_desc()
	autt.scoll_to_find('Force Lock').click()
	sleep(1)
	autt.presskeyevent('KEYCODE_POWER')
	sleep(0.5)
	autt.move_unlock(130)
	autt.remove_desc()
	autt.press_pass()

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
	os.system("adb -s {phone} shell svc power stayon false".format(phone=autt.phone))


