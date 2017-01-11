#!/usr/bin/python3


import os
import sys
if len(sys.argv)==1:
	os.system('/home/da/cts/6.0/android-cts/tools/cts-tradefed')
elif sys.argv[1]=='5':
	os.system('/home/da/cts/5.1/android-cts/tools/cts-tradefed')
elif sys.argv[1]=='6':
	os.system('/home/da/cts/6.0/android-cts/tools/cts-tradefed')
elif sys.argv[1]=='n5':
	os.system('/home/da/new/cts/5.1/android-cts/tools/cts-tradefed')
elif sys.argv[1]=='n6':
	os.system('/home/da/new/cts/6.0/android-cts/tools/cts-tradefed')
elif sys.argv[1]=='gts':
	os.system('/home/da/android-gts/tools/gts-tradefed')
else:
	print('what?')
