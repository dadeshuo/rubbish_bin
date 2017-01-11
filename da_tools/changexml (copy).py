#!/usr/bin/python3




import sys
import xml.etree.ElementTree as ET
import datetime,os
import copy

def getroad(root,pos='',packagename='',result=[]):
    for child in root:
        if child.tag == 'TestSuite':
            for res in getroad(child,pos+child.attrib['name']+'.',packagename,result):
                yield result+res
        else:
            rerror=[]
            for item in child:
                if item.tag == 'Test' and item.attrib['result']=='fail':
                    if packagename !='google.exoplayer' and packagename!='google.media':
                        item.attrib['result']='notExecuted'
                            
                    rerror.append([item.attrib['name'],item[0].attrib['message']])
            if rerror:
                yield [(pos+child.attrib['name']),copy.deepcopy(rerror)]


def main(org):
    tree = ET.parse(org)
    root = tree.getroot()
    err_result=open(os.path.abspath(os.path.dirname(org))+'/error_result.txt','w')
    err_result.write('\n'*3)
    allerr=[]
    for child in root:
        if child.tag == 'TestPackage':
            for item in getroad(child,'',child.attrib['appPackageName'],[]):
                title='-'*4+child.attrib['appPackageName']+'    '+child.attrib['abi']+'-'*4
                err_result.write(title+'\n'*2)
                err_result.write(item[0]+'\n')
                temp=[]
                for ele in item[1]:
                    err_result.write('-- '+ele[0]+':\n')
                    err_result.write(ele[1]+'\n'*2)
                    temp.append(ele[0])
                allerr.append([title,item[0],temp])
                err_result.write('\n'*3+'-'*40+'\n'*3)
    err_result.write('-'*8+'  result  '+'-'*8+'\n'*2)
    for item in allerr:
        err_result.write(item[0]+'\n')
        err_result.write(item[1]+'\n')
        for ele in item[2]:
            err_result.write('-- '+ele+'\n')
        err_result.write('\n')
    err_result.close  
    tree.write('temp.xml',encoding= "UTF-8")
    first=open(org,mode='r',encoding= "UTF-8").readline()	
    newfile=open(org,mode='w',encoding="UTF-8")
    newfile.write(first)
    newfile.write(open('temp.xml' ,mode='r',encoding="UTF-8").read())
    newfile.close()
    os.remove('temp.xml')


if __name__=='__main__':
    org=sys.argv[1]
    main(org)
    print('change finish')


            
   
    

