#!/usr/bin/python3
import traceback,os,re
from functools import wraps,partial
from autotest import getphone
from time import sleep



def traceback_test(func=None,*,act='apk/activity',phone='deviceid'):
	if func==None:
		return partial(traceback_test,act=act,phone=phone)
	pac=act.split('/')[0]

	@wraps(func)
	def wrapper(*args,**kargs):
		try:
			print('\n',func.__name__,' start!\n')
			func(*args,**kargs)
			#print(func.__name__)
			
		except Exception as err:
			detail_err=traceback.format_exc()
			print(err)
			print(detail_err)
		finally: 
			os.system("adb -s {phone} shell am force-stop {pac}  > /dev/null".format(phone=phone,pac=pac))
			sleep(0.5)
			os.system("adb -s {phone} shell am start -S {act}  > /dev/null".format(phone=phone,act=act))
			sleep(1)
			print('\n',func.__name__,' finish!\n')
	return wrapper


