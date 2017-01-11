#!/usr/bin/python3
import re,os
from time import sleep


def getphone():
	out = os.popen("adb devices|grep '\<device\>'").read()
	test=out.split('\n')
	phone_id_all=[]
	for item in test[:-1]:
		phone_id_all.append(item.split( '\t')[0])
	if len(phone_id_all)==1:		
		return phone_id_all[0]

def getsize(phone):
	out = os.popen("adb -s {phone} shell wm size".format(phone=phone)).read()
	pattern = re.compile( r'\d+' )
	return pattern.findall(out)

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


deviceID="VOYD7LO7AYIVGUSC"
ver_apk='com.android.cts.verifier/com.android.cts.verifier.CtsVerifierActivity'
ver_loca='/home/da/android-cts-verifier/6.0/CtsVerifier.apk'
setting_apk=['com.android.settings','com.android.settings/com.android.settings.GnSettingsTabActivity']
camera_apk=['com.android.camera','com.android.camera/com.android.camera.CameraLauncher']
ver_permission_loca='/home/da/android-cts-verifier/6.0/CtsPermissionApp.apk'






class auto_test:

	def __init__(self,dr,phone):
		self.phone=phone
		self.dr=dr
		self.size=getsize(self.phone)
		self.max_x=int(self.size[0])*0.8
		self.min_x=int(self.size[0])*0.3
		self.cen_x=int(self.size[0])*0.5
		self.max_y=int(self.size[1])*0.8
		self.min_y=int(self.size[1])*0.3
		self.cen_y=int(self.size[1])*0.5
		os.system( 'adb -s {phone} shell mkdir /sdcard/verifier_autotest  > /dev/null'.format(phone=self.phone))

	
	def getact(self):
		out = os.popen("adb -s {phone} shell dumpsys window w | grep / |grep name=".format(phone=self.phone)).read()
		pattern = re.compile( r"(?<=name=).*(?=\))" )
		return pattern.findall(out)[0]


	def move(self,phone,x1,y1,x2,y2,time):
		os.system("adb -s {phone} shell  input swipe {x1} {y1} {x2} {y2} {time}".format(phone=phone,x1=x1,y1=y1,x2=x2,y2=y2,time=time))
	
	def move_down(self,time=100):
		self.move(self.phone,self.cen_x,self.cen_y,self.cen_x,self.max_y,time)

	def move_up(self,time=100):
		self.move(self.phone,self.cen_x,self.max_y,self.cen_x,self.cen_y,time)
	
	def move_left(self,time=100):
		self.move(self.phone,self.cen_x,self.cen_y,self.min_x,self.cen_y,time)

	def move_right(self,time=100):
		self.move(self.phone,self.cen_x,self.cen_y,self.max_x,self.cen_y,time)
	
	def move_notice(self):
		self.move(self.phone,self.cen_x,0,self.max_x,self.cen_y,100)

	def move_unlock(self,time=120):
		self.move(self.phone,self.cen_x,self.max_y,self.cen_x,self.min_y,time)
	

	def scoll_to_find(self,name):
		ele=None
		count=0
		while True:
			try:
				ele=self.dr.find_element_by_name(name)		
				break
			except Exception:
				count+=1
				if count > 30:
					raise Exception("can't find "+name)
				sleep(0.5)
				self.move_up(220)
				sleep(1)
		return ele

	def get_all_elewant(self,class_name,attr):
		dic={}
		for ele in self.dr.find_elements_by_class_name(class_name):
			dic[ele.get_attribute(attr)]=ele
		return dic
	
	def open_setting(self):
		os.system("adb -s {phone} shell am start -S {setting_apk}  > /dev/null".format(phone=self.phone,setting_apk=setting_apk[1]))

	def close_setting(self):
		os.system("adb -s {phone} shell am force-stop {setting_apk}  > /dev/null".format(phone=self.phone,setting_apk=setting_apk[0]))

	def open_camera(self):
		os.system("adb -s {phone} shell am start -S {camera_apk}  > /dev/null".format(phone=self.phone,camera_apk=camera_apk[1]))
	
	def close_camera(self):
		os.system("adb -s {phone} shell am force-stop {camera_apk}  > /dev/null".format(phone=self.phone,camera_apk=camera_apk[0]))
		
	def press_shut(self):
		self.dr.find_element_by_id('com.android.camera:id/shutter_button_container').click()


	def remove_desc(self):
		try:
			self.dr.find_element_by_class_name('android.widget.FrameLayout')
			self.dr.find_element_by_name('OK').click()
		except Exception:
			pass

	def allow_permission(self):
		try:
			while True:
				self.dr.find_element_by_class_name('android.widget.FrameLayout')
				self.dr.find_element_by_name('Allow').click()
		except Exception:
			pass

	def creat_folder(self,folder):
		try:
			os.system( 'adb -s {phone} shell mkdir /sdcard/verifier_autotest/{folder}  > /dev/null'.format(phone=self.phone,folder=folder))
		except Exception:
			pass


	def screencap(self,folder,name):
		sleep(0.5)
		print('screencap ',name)
		os.system('adb -s {phone} shell screencap -p "/sdcard/verifier_autotest/{folder}/{name}.png"'.format(phone=self.phone,folder=folder,name=name))
		#self.dr.get_screenshot_as_file('/home/da/appium_screencap/{folder}/{name}.png'.format(folder=folder,name=name))
		print('screencap ',name,' finish')
		sleep(0.5)

	def presskeyevent(self,keyevent):
		sleep(0.5)
		os.system('adb -s {phone} shell input keyevent {keyevent}'.format(phone=self.phone,keyevent=keyevent))

	def press_pass(self):
		passbot=self.dr.find_element_by_id('com.android.cts.verifier:id/pass_button')
		if passbot.is_enabled():
			passbot.click()
			print("test pass")
		else:
			self.press_fail()
			raise Exception("test fail")

	def press_fail(self):
		failbot=self.dr.find_element_by_id('com.android.cts.verifier:id/fail_button')
		if failbot.is_enabled():
			failbot.click()
			print("test fail!")
		else:
			raise Exception("can't press fail ")

	def close_error(self):
		try:
			self.dr.find_element_by_class_name('android.widget.FrameLayout')
			self.dr.find_element_by_name('close').click()
		except Exception:
			pass
'''
	
	def press_pass(self):
		while True:
			buttom=self.dr.find_elements_by_class_name('android.widget.ImageButton')[0]
			if buttom.is_enabled():
				button.click()
				break
			else:
				sleep(1)

	def press_fail(self):
		while True:
			buttom=self.dr.find_elements_by_class_name('android.widget.ImageButton')[2]
			if buttom.is_enabled():
				button.click()
				break
			else:
				sleep(1)

'''

#if __name__=='__main__':

	
		
