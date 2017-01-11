#!/usr/bin/python3

from time import sleep
import os
from debug_test import traceback_test
from autotest import ver_apk,deviceID

#Projection Scrolling List Test
@traceback_test(act=ver_apk,phone=deviceID)
def Projection_Scrolling_List_Test(autt):
	autt.close_error()
	autt.creat_folder('Projection')
	autt.scoll_to_find('Projection Scrolling List Test').click()
	autt.remove_desc()
	autt.screencap('Projection','Projection_Scrolling_List_Test_0')
	for i in range(5):
		autt.move_up()
	autt.screencap('Projection','Projection_Scrolling_List_Test_1')
	autt.press_pass()
	




#Projection Offscreen Activity
@traceback_test(act=ver_apk,phone=deviceID)
def Projection_Offscreen_Activity(autt):
	autt.close_error()
	autt.scoll_to_find('Projection Offscreen Activity').click()
	autt.remove_desc()
	autt.presskeyevent('KEYCODE_POWER')
	sleep(8)
	autt.presskeyevent('KEYCODE_POWER')
	autt.move_unlock(150)
	dic=autt.get_all_elewant('android.widget.TextView','text')
	if list(filter(lambda x:'Success' in x,dic.keys()))!=[]:
		autt.press_pass()
	else:
		autt.press_fail()



#Projection Widget Test
@traceback_test(act=ver_apk,phone=deviceID)
def Projection_Widget_Test(autt):
	autt.close_error()
	autt.creat_folder('Projection')
	autt.scoll_to_find('Projection Widget Test').click()
	autt.remove_desc()
	autt.scoll_to_find('Up').click()
	autt.screencap('Projection','Projection_Widget_Test_0')
	for i in range(3):
		autt.scoll_to_find('Down').click()
		sleep(0.5)
	autt.screencap('Projection','Projection_Widget_Test_1')
	autt.press_pass()
