#!/usr/bin/python3

from time import sleep
import os
from debug_test import traceback_test
from autotest import ver_apk,deviceID

#Camera Formats
@traceback_test(act=ver_apk,phone=deviceID)
def Camera_Formats(autt):
	autt.close_error()
	autt.scoll_to_find('Camera Formats').click()
	autt.creat_folder('Camera_Formats')
	autt.remove_desc()
	def size(camera,NXY):
		last_click=''
		all_item=[]
		while all_item==[] or last_click !=all_item[-1]:
			if all_item!=[]:
				last_click=all_item[-1]
			autt.dr.find_elements_by_class_name('android.widget.Spinner')[1].click()
			itemlis=autt.dr.find_elements_by_class_name('android.widget.TextView')
			for item in itemlis:
				item_name=item.get_attribute('text')
				if  item_name not in all_item:
					all_item.append(item_name)
					item.click()
					sleep(1.5)
					autt.screencap(folder='Camera_Formats',name=(camera+'_'+NXY+'_'+item_name).replace(' ',''))
					break
		autt.presskeyevent('KEYCODE_BACK')

	def move_to_first():
		autt.dr.find_elements_by_class_name('android.widget.Spinner')[1].click()
		lis=autt.dr.find_element_by_class_name('android.widget.ListView')
		lisx=lis.location.get('x')
		lisy=lis.location.get('y')
		lish=lis.size.get('height')
		lisw=lis.size.get('width')
		for i in range(10):
			autt.dr.swipe(lisx+0.5*lisw,lisy+0.25*lish,lisx+0.5*lisw,lisy+0.75*lish)
		autt.dr.find_elements_by_class_name('android.widget.TextView')[0].click()
		

	def NXY(camera):
		autt.dr.find_elements_by_class_name('android.widget.Spinner')[2].click()
		NXY0=autt.dr.find_elements_by_class_name('android.widget.TextView')[0]
		NXY0.click()
		size(camera,'NV')
		move_to_first()
		autt.dr.find_elements_by_class_name('android.widget.Spinner')[2].click()
		NXY1=autt.dr.find_elements_by_class_name('android.widget.TextView')[1]
		NXY1.click()
		size(camera,'YV')
		move_to_first()

	def camera():
		autt.dr.find_elements_by_class_name('android.widget.Spinner')[0].click()
		cam0=autt.dr.find_elements_by_class_name('android.widget.TextView')[0]
		cam0.click()
		NXY('cam0')
		autt.dr.find_elements_by_class_name('android.widget.Spinner')[0].click()
		cam1=autt.dr.find_elements_by_class_name('android.widget.TextView')[1]
		cam1.click()
		NXY('cam1')
		autt.press_pass()
	
	camera()
	
		
#Camera ITS Test
@traceback_test(act=ver_apk,phone=deviceID)
def Camera_ITS_Test(autt):
	autt.close_error()
	autt.scoll_to_find('Camera ITS Test').click()
	sleep(1)

#Camera Intents
@traceback_test(act=ver_apk,phone=deviceID)
def Camera_Intents(autt):
	autt.close_error()
	autt.scoll_to_find('Camera Intents').click()
	autt.remove_desc()
	#photo
	autt.scoll_to_find('Start Test').click()
	autt.open_camera()
	autt.scoll_to_find('Photo').click()
	sleep(0.5)
	autt.press_shut()
	sleep(1)
	autt.close_camera()
	autt.press_pass()
	#video
	autt.scoll_to_find('Start Test').click()
	autt.open_camera()
	autt.scoll_to_find('Video').click()
	sleep(2)
	autt.press_shut()
	sleep(2)
	autt.press_shut()
	autt.close_camera()
	autt.press_pass()

	#camera_i
	autt.scoll_to_find('Start Test').click()
	sleep(2)
	autt.press_shut()
	sleep(2)
	autt.dr.find_element_by_id('com.android.camera:id/review_btn_done').click()
	autt.press_pass()

	#video_i
	autt.scoll_to_find('Start Test').click()
	sleep(2)
	autt.press_shut()
	sleep(2)
	autt.press_shut()
	sleep(2)
	autt.dr.find_element_by_id('com.android.camera:id/review_btn_done').click()
	autt.press_pass()

#Camera Orientation
@traceback_test(act=ver_apk,phone=deviceID)
def Camera_Orientation(autt):
	autt.close_error()
	autt.scoll_to_find('Camera Orientation').click()
	autt.creat_folder('Camera_Orientation')
	autt.remove_desc()
	for i in range(8):
		sleep(1)
		autt.dr.find_element_by_name('Take Photo').click()
		sleep(1)
		autt.screencap(folder='Camera_Orientation',name=str(i+1))
		autt.press_pass()

#Camera Video
@traceback_test(act=ver_apk,phone=deviceID)
def Camera_Video(autt):
	autt.close_error()
	autt.scoll_to_find('Camera Video').click()
	autt.creat_folder('Camera_Video')
	autt.remove_desc()
	def size(camera):
		last_click=''
		all_item=[]
		while all_item==[] or last_click !=all_item[-1]:
			if all_item!=[]:
				last_click=all_item[-1]
			autt.dr.find_elements_by_class_name('android.widget.Spinner')[1].click()
			itemlis=autt.dr.find_elements_by_class_name('android.widget.TextView')
			for item in itemlis:
				item_name=item.get_attribute('text')
				if  item_name not in all_item:
					all_item.append(item_name)
					item.click()
					autt.scoll_to_find('Test').click()
					sleep(8)
					autt.screencap(folder='Camera_Video',name=(camera+'_'+item_name).replace(' ',''))
					break
		autt.presskeyevent('KEYCODE_BACK')

	def camera():
		autt.dr.find_elements_by_class_name('android.widget.Spinner')[0].click()
		cam0=autt.dr.find_elements_by_class_name('android.widget.TextView')[0]
		cam0.click()
		size('cam0')
		autt.dr.find_elements_by_class_name('android.widget.Spinner')[0].click()
		cam1=autt.dr.find_elements_by_class_name('android.widget.TextView')[1]
		cam1.click()
		size('cam1')
		autt.press_pass()
	camera()

