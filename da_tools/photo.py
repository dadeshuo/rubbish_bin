#!/usr/bin/python3

from appium import webdriver
from time import sleep
import os,subprocess,threading
import signal

def getphone():
	out = os.popen("adb devices|grep '\<device\>'").read()
	test=out.split('\n')
	phone_id_all=[]
	for item in test[:-1]:
		phone_id_all.append(item.split( '\t')[0])
	return phone_id_all

package=['com.android.camera','.CameraLauncher']
def_port=10000
bp_port=4700
############################  
class device:
	def __init__(self,deviceID):
		self.desired_caps = {}
		self.desired_caps['deviceName'] = deviceID
		self.desired_caps['platformName'] = 'Android'
		self.desired_caps['platformVersion'] = '6.0'
		#self.desired_caps["unicodeKeyboard"] = "True"
		#self.desired_caps["resetKeyboard"] = "True"
		self.desired_caps['appPackage'] = package[0]
		self.desired_caps['appActivity'] = package[1]
		self.desired_caps['udid']= deviceID
		os.system("adb -s {phone} shell settings put system screen_off_timeout 1800000".format(phone=deviceID))#30min screen_off

	
def test(device):
	print(device.desired_caps)
	print(device.port)
	dr = webdriver.Remote('http://0.0.0.0:{port}/wd/hub'.format(port=device.port), device.desired_caps)	
	sleep(2)
	for i in range(20):
		dr.find_element_by_id('com.android.camera:id/shutter_button_container').click()
		sleep(2)
		dr.find_element_by_id('com.android.camera:id/camera_picker').click()
		sleep(2)
	dr.quit()


if __name__=='__main__':
	id_list=getphone()
	device_list=[]
	Pop_list=[]
	thread_list=[]
	for i, element in enumerate(id_list):
		dev=device(element)
		dev.port=def_port+i
		bp=bp_port+i
		print(dev.port)
	
		Pop=subprocess.Popen('nohup appium -p {port} -bp {bp}  > /dev/null  2>&1 &'.format(port=dev.port,bp=bp),shell=True)
		device_list.append(dev)
		Pop_list.append(Pop)
	#sleep(1000000)

	#test(device_list[0])
	#'''
	sleep(5)
	for item in device_list:
		thread_list.append(threading.Thread(target=test,  args=(item,)))
	for item in thread_list:
		item.start()
	for item in thread_list:
		item.join()
	#'''

	print('等待appium清理')
	sleep(30)
	for item in Pop_list:
		try:
			os.killpg(os.getpgid(item.pid), signal.SIGTERM)
		except Exception:
    			print('error')
	#'''
