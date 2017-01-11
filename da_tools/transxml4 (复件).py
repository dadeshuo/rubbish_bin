#!/usr/bin/python3


from lxml import etree
import os,sys
import gevent

dir32={}
dir64={}

plan6=["android.JobScheduler",
	"android.aadb",
	"android.acceleration",
	"android.accessibility",
	"android.accessibilityservice",
	"android.accounts",
	"android.admin",
	"android.adminhostside",
	"android.alarmclock",
	"android.animation",
	"android.app",
	"android.app.usage",
	"android.appwidget",
	"android.assist",
	"android.bionic",
	"android.bluetooth",
	"android.calendarcommon",
	"android.calllog",
	"android.camera",
	"android.content",
	"android.core.tests.libcore.package.com",
	"android.core.tests.libcore.package.conscrypt",
	"android.core.tests.libcore.package.dalvik",
	"android.core.tests.libcore.package.harmony_annotation",
	"android.core.tests.libcore.package.harmony_beans",
	"android.core.tests.libcore.package.harmony_java_io",
	"android.core.tests.libcore.package.harmony_java_lang",
	"android.core.tests.libcore.package.harmony_java_math",
	"android.core.tests.libcore.package.harmony_java_net",
	"android.core.tests.libcore.package.harmony_java_nio",
	"android.core.tests.libcore.package.harmony_java_text",
	"android.core.tests.libcore.package.harmony_java_util",
	"android.core.tests.libcore.package.harmony_javax_security",
	"android.core.tests.libcore.package.harmony_logging",
	"android.core.tests.libcore.package.harmony_prefs",
	"android.core.tests.libcore.package.harmony_sql",
	"android.core.tests.libcore.package.jsr166",
	"android.core.tests.libcore.package.libcore",
	"android.core.tests.libcore.package.okhttp",
	"android.core.tests.libcore.package.org",
	"android.core.tests.libcore.package.sun",
	"android.core.tests.libcore.package.tests",
	"android.core.tests.libcore.package.tzdata",
	"android.core.vm-tests-tf",
	"android.database",
	"android.display",
	"android.dpi",
	"android.dpi2",
	"android.dreams",
	"android.drm",
	"android.effect",
	"android.gesture",
	"android.graphics",
	"android.graphics2",
	"android.hardware",
	"android.host.app.usage",
	"android.host.atrace",
	"android.host.dumpsys",
	"android.host.jdwpsecurity",
	"android.host.os",
	"android.host.security",
	"android.host.theme",
	"android.jdwp",
	"android.jni",
	"android.keystore",
	"android.leanbackjank",
	"android.libcorelegacy22",
	"android.location",
	"android.location2",
	"android.media",
	"android.mediastress",
	"android.midi",
	"android.nativemedia.sl",
	"android.nativemedia.xa",
	"android.nativeopengl",
	"android.ndef",
	"android.net",
	"android.net.hostsidenetwork",
	"android.netlegacy22.api",
	"android.netlegacy22.permission",
	"android.opengl",
	"android.openglperf",
	"android.os",
	"android.permission",
	"android.permission2",
	"android.preference",
	"android.preference2",
	"android.print",
	"android.provider",
	"android.renderscript",
	"android.renderscriptlegacy",
	"android.rscpp",
	"android.sax",
	"android.security",
	"android.signature",
	"android.speech",
	"android.systemui",
	"android.telecom",
	"android.telecom2",
	"android.telephony",
	"android.tests.appsecurity",
	"android.tests.cpptools",
	"android.text",
	"android.textureview",
	"android.theme",
	"android.transition",
	"android.tv",
	"android.uiautomation",
	"android.uiautomator",
	"android.uirendering",
	"android.usb",
	"android.usescleartexttraffic-false",
	"android.usescleartexttraffic-true",
	"android.usescleartexttraffic-unspecified",
	"android.util",
	"android.view",
	"android.voiceinteraction",
	"android.voicesettings",
	"android.webkit",
	"android.widget",
	"com.android.cts.browserbench",
	"com.android.cts.dram",
	"com.android.cts.filesystemperf",
	"com.android.cts.jank",
	"com.android.cts.jank2",
	"com.android.cts.opengl",
	"com.android.cts.simplecpu",
	"com.android.cts.tvproviderperf",
	"com.android.cts.ui",
	"com.android.cts.uihost",
	"com.android.cts.videoperf",
	"com.drawelements.deqp.egl",
	"com.drawelements.deqp.gles2",
	"com.drawelements.deqp.gles3",
	"com.drawelements.deqp.gles31",
	"com.drawelements.deqp.gles31.copy_image_compressed",
	"com.drawelements.deqp.gles31.copy_image_mixed",
	"com.drawelements.deqp.gles31.copy_image_non_compressed",
	"zzz.android.monkey"]


plan5=["android.JobScheduler",
	"android.aadb",
	"android.acceleration",
	"android.accessibility",
	"android.accessibilityservice",
	"android.accounts",
	"android.admin",
	"android.adminhostside",
	"android.animation",
	"android.app",
	"android.app.usage",
	"android.appwidget",
	"android.bionic",
	"android.bluetooth",
	"android.calendarcommon",
	"android.content",
	"android.core.tests.libcore.package.com",
	"android.core.tests.libcore.package.conscrypt",
	"android.core.tests.libcore.package.dalvik",
	"android.core.tests.libcore.package.harmony_annotation",
	"android.core.tests.libcore.package.harmony_beans",
	"android.core.tests.libcore.package.harmony_java_io",
	"android.core.tests.libcore.package.harmony_java_lang",
	"android.core.tests.libcore.package.harmony_java_math",
	"android.core.tests.libcore.package.harmony_java_net",
	"android.core.tests.libcore.package.harmony_java_nio",
	"android.core.tests.libcore.package.harmony_java_text",
	"android.core.tests.libcore.package.harmony_java_util",
	"android.core.tests.libcore.package.harmony_javax_security",
	"android.core.tests.libcore.package.harmony_logging",
	"android.core.tests.libcore.package.harmony_prefs",
	"android.core.tests.libcore.package.harmony_sql",
	"android.core.tests.libcore.package.jsr166",
	"android.core.tests.libcore.package.libcore",
	"android.core.tests.libcore.package.okhttp",
	"android.core.tests.libcore.package.org",
	"android.core.tests.libcore.package.sun",
	"android.core.tests.libcore.package.tests",
	"android.core.vm-tests-tf",
	"android.database",
	"android.display",
	"android.dpi",
	"android.dpi2",
	"android.dreams",
	"android.drm",
	"android.effect",
	"android.gesture",
	"android.graphics",
	"android.graphics2",
	"android.hardware",
	"android.host.dumpsys",
	"android.host.jdwpsecurity",
	"android.host.security",
	"android.host.theme",
	"android.jdwp",
	"android.jni",
	"android.keystore",
	"android.location",
	"android.location2",
	"android.media",
	"android.mediastress",
	"android.nativemedia.sl",
	"android.nativemedia.xa",
	"android.nativeopengl",
	"android.ndef",
	"android.net",
	"android.net.hostsidenetwork",
	"android.opengl",
	"android.openglperf",
	"android.os",
	"android.permission",
	"android.permission2",
	"android.preference",
	"android.preference2",
	"android.print",
	"android.provider",
	"android.renderscript",
	"android.renderscriptlegacy",
	"android.rscpp",
	"android.sax",
	"android.security",
	"android.signature",
	"android.speech",
	"android.telephony",
	"android.tests.appsecurity",
	"android.tests.cpptools",
	"android.text",
	"android.textureview",
	"android.theme",
	"android.tv",
	"android.uiautomation",
	"android.uiautomator",
	"android.uirendering",
	"android.usb",
	"android.util",
	"android.view",
	"android.webgl",
	"android.webkit",
	"android.widget",
	"com.android.cts.browserbench",
	"com.android.cts.dram",
	"com.android.cts.filesystemperf",
	"com.android.cts.jank",
	"com.android.cts.opengl",
	"com.android.cts.simplecpu",
	"com.android.cts.tvproviderperf",
	"com.android.cts.ui",
	"com.android.cts.uihost",
	"com.android.cts.videoperf",
	"com.drawelements.deqp.gles3",
	"com.drawelements.deqp.gles31",
	"zzz.android.monkey"]

def getchild(org):
	tree = etree.parse(org)
	root = tree.getroot()
	for child in root:
		if child.tag == 'TestPackage':
			if child.get('abi')=="arm64-v8a":
				dir64[child.get('appPackageName')]=child
			elif child.get('abi')=="armeabi-v7a":	
				dir32[child.get('appPackageName')]=child
def cleaninfo(inputinfo):
    info=list(filter(lambda x:x!='null',set(inputinfo.split(','))))
    if info==[]:
        return 'null'
    else:
        return info[-1]

if __name__=='__main__':
	threads = [gevent.spawn(getchild, i) for i in list(sys.argv[1:])]
	gevent.joinall(threads)
	newtree=etree.parse(sys.argv[1])
	root = newtree.getroot()
	for child in root:
		if child.tag == 'TestPackage':
			root.remove(child)
		elif child.tag == 'DeviceInfo':
			for ele in child:
				if ele.tag == 'PhoneSubInfo':
					ele.set('subscriberId',cleaninfo(ele.get('subscriberId')))
				elif ele.tag == 'BuildInfo':
					ele.set('deviceID',cleaninfo(ele.get('deviceID')))
					ele.set('imei',cleaninfo(ele.get('imei')))
					ele.set('imsi',cleaninfo(ele.get('imsi')))
					if ele.get('androidPlatformVersion')=="23":
						plan=plan6
					elif ele.get('androidPlatformVersion')=="22":
						plan=plan5
						
	for i in plan:
		try:
			root.append(dir64[i])
		except Exception:
			pass
	for i in plan:
		try:
			root.append(dir32[i])
		except Exception:
			pass	

	f=open(os.path.abspath(os.path.dirname(sys.argv[1]))+'/'+'testResult.all'+'.xml','wb')
	f.write(etree.tostring(newtree,encoding= "UTF-8",pretty_print=True,xml_declaration=True))
	f.close()
