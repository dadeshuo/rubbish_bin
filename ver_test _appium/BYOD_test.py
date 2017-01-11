#!/usr/bin/python3

from time import sleep
import os,re
from debug_test import traceback_test
from autotest import ver_apk,deviceID,ver_permission_loca

#BYOD Managed Provisioning
@traceback_test(act=ver_apk,phone=deviceID)
def BYOD_Managed_Provisioning(autt):
	autt.close_error()
	os.system("adb -s {phone} shell svc power stayon true".format(phone=autt.phone))#stay awake
	autt.open_setting()
	autt.scoll_to_find('Notification and Control Center').click()
	autt.scoll_to_find('Notifications in lockscreen').click()
	autt.scoll_to_find('Prompt all new information and hide the contents').click()
	autt.close_setting()

	autt.scoll_to_find('BYOD Managed Provisioning').click()
	autt.remove_desc()
	autt.creat_folder('BYOD_Managed_Provisioning')
	BYOD_act=autt.getact()
	autt.scoll_to_find('Start BYOD provisioning flow').click()
	autt.scoll_to_find('Set up').click()
	autt.scoll_to_find('OK').click()
	sleep(20)

	#Profile owner installed
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Profile_owner_installed(autt):
		autt.close_error()
		autt.scoll_to_find('Profile owner installed').click()
		sleep(1)
	'''
	#Badged work apps visible in Launcher
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Badged_work_apps_visible_in_Launcher(autt):
		pass
	'''

	#Work notification is badged	
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Work_notification_is_badged(autt):
		autt.close_error()
		autt.scoll_to_find('Work notification is badged').click()
		autt.scoll_to_find('Go').click()
		sleep(2)
		
		autt.move_notice()
		try:
			autt.dr.find_element_by_name('This is a notification')
		except Exception:
			autt.dr.find_element_by_id('com.android.systemui:id/hide').click()
		finally:
			sleep(1)
			autt.dr.find_element_by_name('This is a notification')
		autt.screencap(folder='BYOD_Managed_Provisioning',name='01_Work_notification_is_badged')
		autt.presskeyevent('KEYCODE_BACK')
		
		sleep(1)
		autt.scoll_to_find('Pass').click()
		sleep(1)

	#Work status icon is displayed
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Work_status_icon_is_displayed(autt):
		autt.close_error()
		autt.scoll_to_find('Work status icon is displayed').click()
		autt.scoll_to_find('Go').click()
		sleep(0.5)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='02_Work_status_icon_is_displayed')
		autt.scoll_to_find('Finish').click()
		autt.scoll_to_find('Pass').click()
		sleep(1)


	#Work status toast is displayed
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Work_status_toast_is_displayed(autt):
		autt.close_error()
		autt.scoll_to_find('Work status toast is displayed').click()
		autt.scoll_to_find('Go').click()
		autt.presskeyevent('KEYCODE_POWER')
		sleep(1)
		autt.presskeyevent('KEYCODE_POWER')
		autt.move_unlock(150)
		sleep(0.2)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='03_Work_status_toast_is_displayed')
		sleep(0.5)
		autt.scoll_to_find('Finish').click()
		autt.scoll_to_find('Pass').click()
		sleep(1)


	#Profile-aware accounts settings
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Profile_aware_accounts_settings(autt):
		autt.close_error()
		autt.scoll_to_find('Profile-aware accounts settings').click()
		autt.scoll_to_find('Go').click()
		autt.scoll_to_find('Advanced Settings').click()
		autt.scoll_to_find('Accounts').click()
		autt.scoll_to_find('Managed by CTS Verifier')
		sleep(1)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='04_Profile_aware_accounts_settings_0')
		autt.scoll_to_find('More').click()
		autt.screencap(folder='BYOD_Managed_Provisioning',name='04_Profile_aware_accounts_settings_1')
		autt.scoll_to_find('Auto-sync personal data').click()
		autt.screencap(folder='BYOD_Managed_Provisioning',name='04_Profile_aware_accounts_settings_2')
		autt.presskeyevent('KEYCODE_BACK') #remove warning
		autt.presskeyevent('KEYCODE_BACK') #back Advanced Settings
		autt.presskeyevent('KEYCODE_BACK') #back Settings
		autt.presskeyevent('KEYCODE_BACK') #back ver
		autt.scoll_to_find('Pass').click()
		sleep(1)


	#Profile-aware device administrator settings
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Profile_aware_device_administrator_settings(autt):
		autt.close_error()
		autt.scoll_to_find('Profile-aware device administrator settings').click()
		autt.scoll_to_find('Go').click()
		autt.scoll_to_find('Device Administrators').click()
		autt.scoll_to_find('Personal')
		sleep(1)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='05_Profile_aware_device_administrator_settings')
		autt.presskeyevent('KEYCODE_BACK') #back Security
		autt.presskeyevent('KEYCODE_BACK') #back ver
		autt.scoll_to_find('Pass').click()
		sleep(1)


	#Profile-aware trusted credential settings
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Profile_aware_trusted_credential_settings(autt):
		autt.close_error()
		autt.scoll_to_find('Profile-aware trusted credential settings').click()
		autt.scoll_to_find('Go').click()
		autt.scoll_to_find('Trusted credentials').click()
		sleep(3)
		autt.scoll_to_find('Personal')
		sleep(1)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='06_Profile_aware_trusted_credential_settings')
		autt.presskeyevent('KEYCODE_BACK') #back Security
		autt.presskeyevent('KEYCODE_BACK') #back ver
		autt.scoll_to_find('Pass').click()
		sleep(1)


	#Profile-aware app settings
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Profile_aware_app_settings(autt):
		autt.close_error()
		autt.scoll_to_find('Profile-aware app settings').click()
		autt.scoll_to_find('Go').click()
		sleep(2)
		count=0
		while True:
			lis=autt.dr.find_elements_by_name('CTS Verifier')	
			if len(lis)==2:
				sleep(1)
				autt.screencap(folder='BYOD_Managed_Provisioning',name='07_Profile_aware_app_settings')
				break
			else:
				autt.move_up(300)
				count+=1
				if count > 20:
					raise Exception
		autt.presskeyevent('KEYCODE_BACK') #back ver
		autt.scoll_to_find('Pass').click()
		sleep(1)



	#Profile-aware location settings
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Profile_aware_location_settings(autt):
		autt.close_error()
		autt.scoll_to_find('Profile-aware location settings').click()
		autt.scoll_to_find('Go').click()
		autt.scoll_to_find('Work profile')
		sleep(1)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='08_Profile_aware_location_settings')
		autt.presskeyevent('KEYCODE_BACK') #back ver
		autt.scoll_to_find('Pass').click()
		sleep(1)


	#Profile-aware printing settings
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Profile_aware_printing_settings(autt):
		autt.close_error()
		autt.scoll_to_find('Profile-aware printing settings').click()
		autt.scoll_to_find('Go').click()
		autt.dr.find_element_by_class_name('android.widget.Spinner').click()
		autt.scoll_to_find('Personal')
		autt.scoll_to_find('Work')
		sleep(1)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='09_Profile_aware_printing_settings')
		autt.presskeyevent('KEYCODE_BACK') #close Spinner
		autt.presskeyevent('KEYCODE_BACK') #back ver
		autt.scoll_to_find('Pass').click()
		sleep(1)



	#Open app cross profiles from the personal side
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Open_app_cross_profiles_from_the_personal_side(autt):
		autt.close_error()
		autt.scoll_to_find('Open app cross profiles from the personal side').click()
		autt.scoll_to_find('Go').click()
		sleep(1)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='10_Open_app_cross_profiles_from_the_personal_side')
		autt.scoll_to_find('CTS Verifier').click()
		autt.scoll_to_find('Finish').click()
		autt.scoll_to_find('Pass').click()
		sleep(1)


	#Open app cross profiles from the work side
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Open_app_cross_profiles_from_the_work_side(autt):
		autt.close_error()
		autt.scoll_to_find('Open app cross profiles from the work side').click()
		autt.scoll_to_find('Go').click()
		sleep(1)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='11_Open_app_cross_profiles_from_the_work_side')
		autt.scoll_to_find('CTS Verifier').click()
		autt.scoll_to_find('Finish').click()
		autt.scoll_to_find('Pass').click()
		sleep(1)


	#App links from the work side
	@traceback_test(act=BYOD_act,phone=deviceID)
	def App_links_from_the_work_side(autt):
		autt.close_error()
		autt.scoll_to_find('App links from the work side').click()
		autt.scoll_to_find('Go').click()
		sleep(1)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='12_App_links_from_the_work_side_0')
		autt.scoll_to_find('CTS Verifier').click()
		autt.scoll_to_find('Finish').click()
		autt.scoll_to_find('Go').click()
		autt.scoll_to_find('Personal').click()
		sleep(1)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='12_App_links_from_the_work_side_1')
		#autt.scoll_to_find('CTS Verifier').click()
		#autt.scoll_to_find('Finish').click()
		autt.presskeyevent('KEYCODE_BACK')
		autt.scoll_to_find('Pass').click()
		sleep(1)

	#Disable non-market apps
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Disable_non_market_apps(autt):
		autt.close_error()
		autt.scoll_to_find('Disable non-market apps').click()
		autt.scoll_to_find('Go').click()
		sleep(1)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='13_Disable_non_market_apps')
		autt.scoll_to_find('Install blocked')
		autt.scoll_to_find('OK').click()
		autt.scoll_to_find('Pass').click()
		sleep(1)



	#Enable non-market apps
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Enable_non_market_apps(autt):
		autt.close_error()
		autt.scoll_to_find('Enable non-market apps').click()
		autt.scoll_to_find('Go').click()
		sleep(1)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='14_Enable_non_market_apps')
		autt.scoll_to_find('Install').click()
		autt.scoll_to_find('Pass').click()
		sleep(1)


	#Cross profile intent filters are set
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Cross_profile_intent_filters_are_set(autt):
		autt.close_error()
		autt.scoll_to_find('Cross profile intent filters are set').click()
		sleep(1)


	#Permissions lockdown
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Permissions_lockdown(autt):
		autt.close_error()
		os.system("adb -s {phone} install -r '{ver_permission_loca}'".format(phone=autt.phone,ver_permission_loca=ver_permission_loca))
		sleep(1)
		autt.scoll_to_find('Permissions lockdown').click()
		autt.scoll_to_find('Go').click()
		#Grant
		autt.scoll_to_find('Grant').click()
		autt.scoll_to_find('Open Application Settings').click()
		sleep(1)
		if autt.scoll_to_find('Contacts'):
			autt.scoll_to_find('Permissions').click()
			if  autt.scoll_to_find('Contacts').is_enabled()== False:
				autt.presskeyevent('KEYCODE_BACK') #back app
				autt.presskeyevent('KEYCODE_BACK') #back ver
			else:
				raise Exception('Permissions lockdown fail')
		else:
			raise Exception('Permissions lockdown fail')

		#Let user decide
		autt.scoll_to_find('Let user decide').click()
		autt.scoll_to_find('Open Application Settings').click()
		sleep(1)
		if autt.scoll_to_find('Contacts'):
			autt.scoll_to_find('Permissions').click()
			if  autt.scoll_to_find('Contacts').is_enabled()== True:
				autt.presskeyevent('KEYCODE_BACK') #back app
				autt.presskeyevent('KEYCODE_BACK') #back ver
			else:
				raise Exception('Permissions lockdown fail')
		else:
			raise Exception('Permissions lockdown fail')

		#Deny
		autt.scoll_to_find('Deny').click()
		autt.scoll_to_find('Open Application Settings').click()
		sleep(1)
		if autt.scoll_to_find('No permissions granted'):
			autt.scoll_to_find('Permissions').click()
			if  autt.scoll_to_find('Contacts').is_enabled()== False:
				autt.presskeyevent('KEYCODE_BACK') #back app
				autt.presskeyevent('KEYCODE_BACK') #back ver
			else:
				raise Exception('Permissions lockdown fail')
		else:
			raise Exception('Permissions lockdown fail')
	
		autt.scoll_to_find('Finish').click()
		autt.scoll_to_find('Pass').click()
		sleep(1)
	

	#Vpn test
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Vpn_test(autt):
		autt.close_error()
		autt.remove_desc()
		autt.scoll_to_find('Vpn test').click()
		autt.scoll_to_find('OK').click()
		sleep(1)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='15_Vpn_test')
		autt.press_pass()
		sleep(1)


	#Disallow apps control
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Disallow_apps_control(autt):
		autt.close_error()
		autt.scoll_to_find('Disallow apps control').click()
		autt.remove_desc()
		autt.scoll_to_find('Prepare test').click()
		sleep(1)
		autt.scoll_to_find('Disabled uninstall button').click()
		autt.scoll_to_find('Go').click()
		sleep(5)
		autt.scoll_to_find('All apps').click()
		autt.scoll_to_find('Work').click()
		sleep(5)
		autt.scoll_to_find('CTS Verifier').click()
		if autt.scoll_to_find('Uninstall').is_enabled()==False and autt.scoll_to_find('Force stop').is_enabled()==False:
			sleep(1)
			autt.screencap(folder='BYOD_Managed_Provisioning',name='16_Disallow_apps_control_0')
			autt.scoll_to_find('Storage').click()
			if autt.scoll_to_find('Clear data').is_enabled()==False and autt.scoll_to_find('Clear cache').is_enabled()==False:
				sleep(1)
				autt.screencap(folder='BYOD_Managed_Provisioning',name='16_Disallow_apps_control_1')
				autt.presskeyevent('KEYCODE_BACK') #back app info
				autt.presskeyevent('KEYCODE_BACK') #back app
				autt.presskeyevent('KEYCODE_BACK') #back ver
			else:
				raise Exception('Permissions lockdown fail')
		else:
			raise Exception('Permissions lockdown fail')
		autt.scoll_to_find('Pass').click()
		autt.scoll_to_find('Disabled force stop button').click()
		autt.scoll_to_find('Pass').click()
		autt.scoll_to_find('Disabled app storage buttons').click()
		autt.scoll_to_find('Pass').click()
		autt.press_pass()
		sleep(1)


	#Camera support cross profile image capture
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Camera_support_cross_profile_image_capture(autt):
		autt.close_error()
		autt.scoll_to_find('Camera support cross profile image capture').click()
		autt.scoll_to_find('Go').click()
		sleep(10)
		autt.press_shut()
		sleep(1)
		autt.dr.find_element_by_id('com.android.camera:id/review_btn_done').click()
		sleep(2)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='17_Camera_support_cross_profile_image_capture')
		autt.scoll_to_find('Close').click()
		autt.scoll_to_find('Pass').click()
		sleep(1)

	#Camera support cross profile video capture (with extra output path)
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Camera_support_cross_profile_video_capture_with_extra_output_path(autt):
		autt.close_error()
		autt.scoll_to_find('Camera support cross profile video capture (with extra output path)').click()
		autt.scoll_to_find('Go').click()
		sleep(3)
		autt.press_shut()
		sleep(2)
		autt.press_shut()
		sleep(1)
		autt.dr.find_element_by_id('com.android.camera:id/review_btn_done').click()
		autt.scoll_to_find('Play').click()
		sleep(3)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='18_Camera_support_cross_profile_video_capture_with_extra_output_path')
		autt.scoll_to_find('Close').click()
		autt.scoll_to_find('Pass').click()
		sleep(1)

	
	#Camera support cross profile video capture (without extra output path)
	@traceback_test(act=BYOD_act,phone=deviceID)
	def Camera_support_cross_profile_video_capture_without_extra_output_path(autt):
		autt.close_error()
		autt.scoll_to_find('Camera support cross profile video capture (without extra output path)').click()
		autt.scoll_to_find('Go').click()
		sleep(3)
		autt.press_shut()
		sleep(2)
		autt.press_shut()
		sleep(1)
		autt.dr.find_element_by_id('com.android.camera:id/review_btn_done').click()
		autt.scoll_to_find('Play').click()
		sleep(3)
		autt.screencap(folder='BYOD_Managed_Provisioning',name='19_Camera_support_cross_profile_video_capture_without_extra_output_path')
		autt.scoll_to_find('Close').click()
		autt.scoll_to_find('Pass').click()
		sleep(1)	



	Profile_owner_installed(autt)
	####Badged_work_apps_visible_in_Launcher(autt)
	#'''
	Work_notification_is_badged(autt)
	Work_status_icon_is_displayed(autt)
	Work_status_toast_is_displayed(autt)
	Profile_aware_accounts_settings(autt)
	Profile_aware_device_administrator_settings(autt)
	Profile_aware_trusted_credential_settings(autt)
	Profile_aware_app_settings(autt)
	Profile_aware_location_settings(autt)
	Profile_aware_printing_settings(autt)
	Open_app_cross_profiles_from_the_personal_side(autt)
	Open_app_cross_profiles_from_the_work_side(autt)
	App_links_from_the_work_side(autt)
	Disable_non_market_apps(autt)
	Enable_non_market_apps(autt)
	Cross_profile_intent_filters_are_set(autt)
	#'''
	Permissions_lockdown(autt)
	#'''
	Vpn_test(autt)
	Disallow_apps_control(autt)
	
	Camera_support_cross_profile_image_capture(autt)
	Camera_support_cross_profile_video_capture_with_extra_output_path(autt)
	Camera_support_cross_profile_video_capture_without_extra_output_path(autt)
	#'''
	os.system("adb -s {phone} shell svc power stayon false".format(phone=autt.phone))#stay awake
	autt.presskeyevent('KEYCODE_BACK')



#Device Owner Provisioning
@traceback_test(act=ver_apk,phone=deviceID)
def Device_Owner_Provisioning(autt):
	autt.close_error()
	autt.scoll_to_find('Device Owner Provisioning').click()
	autt.remove_desc()
	autt.scoll_to_find('Device owner negative test').click()
	autt.scoll_to_find('Start provisioning').click()
	sleep(1)
	autt.remove_desc()
	autt.press_pass()
	autt.press_pass()

 
#Device Owner Tests
@traceback_test(act=ver_apk,phone=deviceID)
def Device_Owner_Tests(autt):
	autt.close_error()
	autt.scoll_to_find('Device Owner Tests').click()
	autt.remove_desc()
	os.system("adb -s {phone} shell svc power stayon true".format(phone=autt.phone))#stay awake
	os.system("adb -s {phone} shell dpm set-device-owner 'com.android.cts.verifier/com.android.cts.verifier.managedprovisioning.DeviceAdminTestReceiver'".format(phone=autt.phone))#vercmd
	DOT_act=autt.getact()
	autt.scoll_to_find('Check device owner').click()
	autt.creat_folder('Device_Owner_Tests')

	
	

	#Device administrator settings
	@traceback_test(act=DOT_act,phone=deviceID)
	def Device_administrator_settings(autt):
		autt.close_error()
		autt.scoll_to_find('Device administrator settings').click()
		autt.remove_desc()
		autt.scoll_to_find('Go').click()
		autt.scoll_to_find('Device Administrators').click()
		if not autt.scoll_to_find('CTS Verifier').is_enabled():
			autt.screencap(folder='Device_Owner_Tests',name='Device_administrator_settings')
			autt.presskeyevent('KEYCODE_BACK')
			autt.presskeyevent('KEYCODE_BACK')
			autt.press_pass()
	
	#WiFi configuration lockdown
	@traceback_test(act=DOT_act,phone=deviceID)
	def WiFi_configuration_lockdown(autt):
		autt.close_error()
		autt.scoll_to_find('WiFi configuration lockdown').click()
		autt.remove_desc()
		autt.dr.find_element_by_id('com.android.cts.verifier:id/device_owner_wifi_ssid').send_keys(u'chengxd')
		sleep(1)
		autt.scoll_to_find('None').click()
		sleep(1)
		autt.scoll_to_find('Create WiFi configuration').click()
		sleep(1)
		
		autt.scoll_to_find('Unlocked config is modifiable in Settings').click()
		autt.scoll_to_find('WiFi config lockdown off').click()
		autt.scoll_to_find('Go to WiFi Settings').click()
		sleep(10)
		autt.scoll_to_find('chengxd').click()
		sleep(1)
		autt.screencap(folder='Device_Owner_Tests',name='Unlocked_config_is_modifiable_in_Settings')
		autt.presskeyevent('KEYCODE_BACK')
		autt.presskeyevent('KEYCODE_BACK')
		autt.press_pass()
		
		autt.scoll_to_find('Locked config is not modifiable in Settings').click()
		autt.scoll_to_find('WiFi config lockdown on').click()
		autt.scoll_to_find('Go to WiFi Settings').click()
		sleep(10)
		autt.scoll_to_find('chengxd').click()
		sleep(1)
		autt.screencap(folder='Device_Owner_Tests',name='Locked_config_is_not_modifiable_in_Settings')
		autt.presskeyevent('KEYCODE_BACK')
		autt.presskeyevent('KEYCODE_BACK')
		autt.press_pass()

		autt.scoll_to_find('Locked config can be connected to').click()
		autt.scoll_to_find('WiFi config lockdown on').click()
		autt.scoll_to_find('Go to WiFi Settings').click()
		sleep(10)
		autt.scoll_to_find('chengxd').click()
		sleep(1)
		autt.screencap(folder='Device_Owner_Tests',name='Locked_config_can_be_connected_to')
		autt.presskeyevent('KEYCODE_BACK')
		autt.presskeyevent('KEYCODE_BACK')
		autt.press_pass()

		autt.scoll_to_find('Unlocked config can be forgotten in Settings').click()
		autt.scoll_to_find('WiFi config lockdown off').click()
		autt.scoll_to_find('Go to WiFi Settings').click()
		sleep(10)
		autt.scoll_to_find('chengxd').click()
		sleep(1)
		autt.screencap(folder='Device_Owner_Tests',name='Unlocked_config_can_be_forgotten_in_Settings')
		autt.presskeyevent('KEYCODE_BACK')
		autt.presskeyevent('KEYCODE_BACK')
		autt.press_pass()
		
		autt.press_pass()

	#Disallow configuring WiFi
	@traceback_test(act=DOT_act,phone=deviceID)
	def Disallow_configuring_WiFi(autt):
		autt.close_error()
		autt.scoll_to_find('Disallow configuring WiFi').click()
		autt.remove_desc()	
		autt.scoll_to_find('Set restriction').click()
		autt.scoll_to_find('Go').click()
		sleep(1)
		autt.screencap(folder='Device_Owner_Tests',name='Disallow_configuring_WiFi')
		autt.presskeyevent('KEYCODE_BACK')
		autt.press_pass()
		

	#Disallow configuring VPN
	@traceback_test(act=DOT_act,phone=deviceID)
	def Disallow_configuring_VPN(autt):
		autt.close_error()
		autt.scoll_to_find('Disallow configuring VPN').click()
		autt.remove_desc()
		autt.scoll_to_find('Set VPN restriction').click()
		sleep(1)
		autt.scoll_to_find('Go').click()
		sleep(1)
		autt.screencap(folder='Device_Owner_Tests',name='Disallow_configuring_VPN_0')
		autt.presskeyevent('KEYCODE_BACK')
		sleep(1)
		autt.scoll_to_find('Check VPN').click()
		sleep(1)
		autt.scoll_to_find('OK').click()
		autt.screencap(folder='Device_Owner_Tests',name='Disallow_configuring_VPN_1')
		autt.press_pass()
		autt.press_pass()

	#Disallow configuring Bluetooth
	@traceback_test(act=DOT_act,phone=deviceID)
	def Disallow_configuring_Bluetooth(autt):
		autt.close_error()
		autt.scoll_to_find('Disallow configuring Bluetooth').click()
		autt.remove_desc()
		autt.scoll_to_find('Set restriction').click()
		autt.scoll_to_find('Go').click()
		sleep(1)
		autt.screencap(folder='Device_Owner_Tests',name='Disallow_configuring_Bluetooth')
		autt.presskeyevent('KEYCODE_BACK')
		autt.press_pass()

	'''
	#Disallow USB file transfer
	@traceback_test(act=DOT_act,phone=deviceID)
	def Disallow_USB_file_transfer(autt):
		autt.close_error()
		autt.scoll_to_find('Disallow USB file transfer').click()
		autt.remove_desc()
		autt.scoll_to_find('Set restriction').click()
		autt.move_notice()
		try:
			autt.dr.find_element_by_name('USB for charging')
		except Exception:
			autt.dr.find_element_by_id('com.android.systemui:id/hide').click()
		finally:
			sleep(1)
			autt.dr.find_element_by_name('USB for charging').click()
		try:
			autt.scoll_to_find('Copy files').click()
		except Exception:
			pass
		sleep(3)
		os.system("adb devices")
		sleep(3)
		autt.move_notice()
		autt.screencap(folder='Device_Owner_Tests',name='Disallow_USB_file_transfer_0')
		autt.dr.find_element_by_name('USB for file transfer').click()
		autt.screencap(folder='Device_Owner_Tests',name='Disallow_USB_file_transfer_1')
		autt.presskeyevent('KEYCODE_BACK')
		autt.press_pass()
	'''
	#Disable status bar
	@traceback_test(act=DOT_act,phone=deviceID)
	def Disable_status_bar(autt):
		autt.close_error()
		autt.scoll_to_find('Disable status bar').click()
		autt.remove_desc()
		autt.screencap(folder='Device_Owner_Tests',name='Disable_status_bar_0')
		sleep(1)
		autt.dr.find_elements_by_class_name('android.widget.Button')[0].click()
		sleep(1)
		autt.screencap(folder='Device_Owner_Tests',name='Disable_status_bar_1')
		sleep(1)
		autt.dr.find_elements_by_class_name('android.widget.Button')[1].click()
		sleep(1)
		autt.screencap(folder='Device_Owner_Tests',name='Disable_status_bar_2')
		autt.press_pass()

	#Disable keyguard
	@traceback_test(act=DOT_act,phone=deviceID)
	def Disable_keyguard(autt):
		autt.close_error()
		autt.scoll_to_find('Disable keyguard').click()
		autt.remove_desc()
		autt.dr.find_elements_by_class_name('android.widget.Button')[0].click()
		sleep(1)
		autt.presskeyevent('KEYCODE_POWER')
		sleep(1)
		autt.presskeyevent('KEYCODE_POWER')
		sleep(0.5)
		autt.screencap(folder='Device_Owner_Tests',name='Disable_keyguard_0')
		autt.move_unlock(130)
		sleep(1)
		autt.dr.find_elements_by_class_name('android.widget.Button')[1].click()
		sleep(1)
		autt.presskeyevent('KEYCODE_POWER')
		sleep(1)
		autt.presskeyevent('KEYCODE_POWER')
		sleep(0.5)
		autt.screencap(folder='Device_Owner_Tests',name='Disable_keyguard_1')
		autt.move_unlock(130)
		sleep(1)
		autt.press_pass()

	#Permissions lockdown
	@traceback_test(act=DOT_act,phone=deviceID)
	def Permissions_lockdown(autt):
		autt.close_error()
		autt.scoll_to_find('Permissions lockdown').click()
		autt.remove_desc()
		autt.open_setting()
		autt.scoll_to_find('More').click()
		autt.scoll_to_find('Airplane Mode').click()
		autt.scoll_to_find('Airplane Mode').click()
		pattern = re.compile( r'\d+' )
		ap_state=pattern.findall(os.popen("adb -s {phone} shell settings list global |grep airplane_mode_on=".format(phone=deviceID)).read())
		if ap_state[0]=='0':
			autt.scoll_to_find('Airplane Mode').click()
		autt.close_setting()
		os.system("adb -s {phone} install -r '{ver_permission_loca}'".format(phone=autt.phone,ver_permission_loca=ver_permission_loca))
		sleep(1)

		#Grant
		autt.scoll_to_find('Grant').click()
		autt.scoll_to_find('Open Application Settings').click()
		sleep(1)
		if autt.scoll_to_find('Contacts'):
			autt.scoll_to_find('Permissions').click()
			if  autt.scoll_to_find('Contacts').is_enabled()== False:
				autt.presskeyevent('KEYCODE_BACK') #back app
				autt.presskeyevent('KEYCODE_BACK') #back ver
			else:
				raise Exception('Permissions lockdown fail')
		else:
			raise Exception('Permissions lockdown fail')

		#Let user decide
		autt.scoll_to_find('Let user decide').click()
		autt.scoll_to_find('Open Application Settings').click()
		sleep(1)
		if autt.scoll_to_find('Contacts'):
			autt.scoll_to_find('Permissions').click()
			if  autt.scoll_to_find('Contacts').is_enabled()== True:
				autt.presskeyevent('KEYCODE_BACK') #back app
				autt.presskeyevent('KEYCODE_BACK') #back ver
			else:
				raise Exception('Permissions lockdown fail')
		else:
			raise Exception('Permissions lockdown fail')

		#Deny
		autt.scoll_to_find('Deny').click()
		autt.scoll_to_find('Open Application Settings').click()
		sleep(1)
		if autt.scoll_to_find('No permissions granted'):
			autt.scoll_to_find('Permissions').click()
			if  autt.scoll_to_find('Contacts').is_enabled()== False:
				autt.presskeyevent('KEYCODE_BACK') #back app
				autt.presskeyevent('KEYCODE_BACK') #back ver
			else:
				raise Exception('Permissions lockdown fail')
		else:
			raise Exception('Permissions lockdown fail')

		autt.press_pass()

	#Remove device owner
	@traceback_test(act=DOT_act,phone=deviceID)
	def Remove_device_owner(autt):
		autt.close_error()
		autt.scoll_to_find('Remove device owner').click()
		autt.remove_desc()	
		autt.dr.find_elements_by_class_name('android.widget.Button')[0].click()
		sleep(1)
		autt.open_setting()
		autt.scoll_to_find('Security').click()
		autt.scoll_to_find('Device Administrators').click()
		if autt.scoll_to_find('CTS Verifier').is_enabled():
			autt.screencap(folder='Device_Owner_Tests',name='Remove_device_owner')
		autt.close_setting()
		autt.press_pass()

	
	autt.open_setting()
	autt.scoll_to_find('WLAN').click()
	sleep(10)
	try:
		autt.dr.find_element_by_name('Off').click()
		sleep(10)
	except Exception:
		autt.close_setting()
	finally:
		autt.close_setting()

	autt.open_setting()
	autt.scoll_to_find('Bluetooth').click()
	sleep(10)
	try:
		autt.dr.find_element_by_name('Off').click()
		sleep(10)
	except Exception:
		autt.close_setting()
	finally:
		autt.close_setting()
	
	Device_administrator_settings(autt)
	WiFi_configuration_lockdown(autt)
	Disallow_configuring_WiFi(autt)
	Disallow_configuring_VPN(autt)
	Disallow_configuring_Bluetooth(autt)
	####Disallow_USB_file_transfer(autt) #APPIUM DIE!!
	Disable_status_bar(autt)
	Disable_keyguard(autt)
	Permissions_lockdown(autt)
	Remove_device_owner(autt)
	autt.presskeyevent('KEYCODE_BACK')
		
