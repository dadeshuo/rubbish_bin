#!/usr/bin/python3


from lxml import etree
import time,os,sys
import copy
import multiprocessing
import getopt

def getroad(root,pos='',opinion=['',''],result=[]):
    for child in root:
        if child.tag == 'TestSuite':
            for res in getroad(child,pos+child.get('name')+'.',opinion,result):
                yield result+res
        else:
            rerror=[]
            for item in child:
                if item.tag == 'Test' and item.get('result')=='fail':
                    if opinion[0] !='google.exoplayer' and opinion[0]!='google.media' and opinion[1]=='change':
                        item.set('result','notExecuted')
                    try:
                        message=item[0].get('message').replace('\t','')
                        more_message=item[0][0].text.replace('\t','')
                    except Exception:
                        message='null'
                        more_message='null'
                    rerror.append([item.get('name'),message,more_message])
            if rerror:
                yield [(pos+child.get('name')),copy.deepcopy(rerror)]

def cleaninfo(inputinfo):
    info=list(filter(lambda x:x!='null',set(inputinfo.split(','))))
    if info==[]:
        return 'null'
    else:
        return info[-1]

class xmlbody():
    def __init__(self,org):
        self.org=org
        self.tree = etree.parse(org)
        self.path=os.path.abspath(os.path.dirname(org))
        with open(self.org,mode='rb') as read_title:
            self.first=read_title.readline()
                    
    def changexml(self,opinion='change'):
        self.change_tree=copy.deepcopy(self.tree)
        root = self.change_tree.getroot()
        self.result=[]
        for child in root:
            if child.tag == 'TestPackage':
                res=list(getroad(child,'',[child.get('appPackageName'),opinion],[]))
                if res!=[]:
                    self.result.append([child.get('appPackageName'),child.get('abi'),res])
            elif child.tag == 'DeviceInfo':
                for ele in child:
                    if ele.tag == 'PhoneSubInfo':
                        ele.set('subscriberId',cleaninfo(ele.get('subscriberId')))
                    if ele.tag == 'BuildInfo':
                        ele.set('deviceID',cleaninfo(ele.get('deviceID')))
                        ele.set('imei',cleaninfo(ele.get('imei')))
                        ele.set('imsi',cleaninfo(ele.get('imsi')))

    def getinfo(self):
        self.info_tree=copy.deepcopy(self.tree)
        root = self.info_tree.getroot()
        for child in root:
            if child.tag == 'TestPackage':
                root.remove(child)
            elif child.tag == 'DeviceInfo':
                for ele in child:
                    if ele.tag == 'PhoneSubInfo':
                        ele.set('subscriberId',cleaninfo(ele.get('subscriberId')))
                    if ele.tag == 'BuildInfo':
                        ele.set('deviceID',cleaninfo(ele.get('deviceID')))
                        ele.set('imei',cleaninfo(ele.get('imei')))
                        ele.set('imsi',cleaninfo(ele.get('imsi')))

    def write_xml(self,name,write_tree):
        f=open(self.path+'/'+name+'.xml','wb')
        f.write(etree.tostring(write_tree,encoding= "UTF-8",pretty_print=True,xml_declaration=True))
        f.close()

 
    def m_output(self):
        with open(self.path+'/m_output.txt', mode='w')as err_result:
            err_result.write('\n'*3)
            for item in self.result:
                err_result.write('package :'+item[0]+'    '+item[1]+'\n'*2)
                for cla in item[2]:
                    err_result.write(cla[0]+'\n')
                    for ele in cla[1]:
                        err_result.write('-- '+ele[0]+':\n')
                        err_result.write(ele[1]+'\n'*2)
                    err_result.write('\n')
                err_result.write('\n'*3+'-'*40+'\n'*3)

    def s_output(self):
        with open(self.path+'/s_output.txt', mode='w')as err_result:
            err_result.write('\n'*3)
            for item in self.result:
                err_result.write('package :'+item[0]+'    '+item[1]+'\n')
                for cla in item[2]:
                    err_result.write(cla[0]+'\n')
                    for ele in cla[1]:
                        err_result.write('-- '+ele[0]+'\n')
                    err_result.write('\n')
                err_result.write('\n'*3+'-'*40+'\n'*3)

    def l_output(self):
        with open(self.path+'/L_output.txt', mode='w')as err_result:
            err_result.write('\n'*3)
            for item in self.result:
                err_result.write('package :'+item[0]+'    '+item[1]+'\n'*2)
                for cla in item[2]:
                    err_result.write(cla[0]+'\n')
                    for ele in cla[1]:
                        err_result.write('-- '+ele[0]+':\n')
                        err_result.write(ele[1]+'\n'*2)
                        err_result.write('#'*40+'\n')
                        err_result.write(ele[2])
                        if list(ele[2])[-1]!='\n':
                            err_result.write('\n')
                        err_result.write('#'*40+'\n'*2)
                    err_result.write('\n')
                err_result.write('\n'*3+'-'*40+'\n'*3)

    def changexml_and_output(self,opion):
        self.changexml(opinion=opion)
        change = multiprocessing.Process(target=self.write_xml, args=('after_change', self.change_tree))
        s_output= multiprocessing.Process(target=self.s_output)
        m_output= multiprocessing.Process(target=self.m_output)
        l_output= multiprocessing.Process(target=self.l_output)
        change.start()
        s_output.start()
        m_output.start()
        l_output.start()
        change.join()
        s_output.join()
        m_output.join()
        l_output.join()
        os.rename(self.org,self.org+'.bak')
        os.rename(self.path+'/'+'after_change'+'.xml',self.org)
        print('changexml finish')

    def get_info_and_output(self):
        self.getinfo()
        get = multiprocessing.Process(target=self.write_xml, args=('info', self.info_tree))
        get.start()
        get.join()
        print('getinfo finish')                



@profile
def main():
    try:
        opts,args= getopt.getopt(sys.argv[1:], "p:o,f:o")
    except getopt.GetoptError as err:
    # print help information and exit:
        print(err) 
        sys.exit(2)

    for o, a in opts:
        if o =='':
            continue
        elif o == "-f":
            org=a

        elif o == "-p":
            plan=a

        else:
            assert False, "unhandled option"

    test=xmlbody(org)
    if plan=='a':
        out1 = multiprocessing.Process(target=test.changexml_and_output,args=('None',))
        out2=  multiprocessing.Process(target=test.get_info_and_output)
        out1.start()
        out2.start()
        out1.join()
        out2.join()
    elif plan=='c':
        out1 = multiprocessing.Process(target=test.changexml_and_output,args=('change',))
        out1.start()
        out1.join()

if __name__=='__main__':
    main()

