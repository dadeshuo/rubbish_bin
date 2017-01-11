#!/usr/bin/python3

import mysql.connector
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time  
import os
import xlsxwriter
from lxml import etree
import sys


def changemeaasge(message):
    if message.startswith('='):
        return "'"+message
    else:
        return message.replace('"',"'")


def bug_filter(org):
    cts= (
    "CREATE TABLE if not exists `cts` ("
    "`abi` varchar(255) NOT NULL,"
    "`module` varchar(255) NOT NULL,"
    "`testcase` varchar(255) NOT NULL,"
    "`test` varchar(255) NOT NULL,"
    "`failure` text NOT NULL,"
    "`stacktrace` text NOT NULL"
    ");")
    cnx = mysql.connector.connect(user='root', password='',database='cts')
    cursor = cnx.cursor()
    cursor.execute('drop tables if exists `cts`;')
    cursor.execute(cts) 
    tree_list = [etree.parse(i) for i in org]
    error_dict={}
    test_case_report={}
    for tree in tree_list:
        for item in etree.XPath(r".//Test[@result='fail']")(tree):
            abi=item.getparent().getparent().get('abi')
            module=item.getparent().getparent().get('name')
            testcase=item.getparent().get('name')
            test=item.get('name')
            failure=changemeaasge(item[0].get('message').replace('\t',''))
            stacktrace=changemeaasge(item[0][0].text.replace('\t',''))
            test_case_report[testcase]=module
            if error_dict.get(testcase+test,None)!=None:
                error_dict[testcase+test]+=','+abi
                cursor.execute("update cts set abi = '{abi}' where testcase= '{testcase}' and test ='{test}'".format(abi=error_dict[testcase+test],testcase=testcase,test=test))
            else:
                add_bug =('''INSERT INTO cts (abi, module, testcase, test, failure, stacktrace) VALUES ("{abi}", "{module}", "{testcase}", "{test}", "{failure}", "{stacktrace}")'''.format(abi=abi,module=module,testcase=testcase,test=test,failure=failure,stacktrace=stacktrace))
                cursor.execute(add_bug)
                error_dict[testcase+test]=abi
    cnx.commit()
    cursor.close()
    cnx.close()
    print(len(error_dict))    
    return test_case_report

def output_excel(org):
    output_path=os.path.abspath(os.path.dirname(org[0]))
    workbook = xlsxwriter.Workbook(output_path+r'/xlsx_output.xlsx')
    worksheet = workbook.add_worksheet()
    row=0
    cnx = mysql.connector.connect(user='root', password='',database='cts')
    cursor = cnx.cursor()
    count_sql="select * from cts "
    cursor.execute(count_sql)
    for (abi, module, testcase, test, failure, stacktrace) in cursor:
        worksheet.write(row,0,abi)
        worksheet.write(row,1,module)
        worksheet.write(row,2,testcase)
        worksheet.write(row,3,test)
        worksheet.write(row,4,failure)
        worksheet.write(row,5,stacktrace)
        row+=1
    print('output excel finish')
    cursor.close()
    cnx.close()
    

if __name__=='__main__':
    org=sys.argv[1:]
    bug_filter(org)
    output_excel(org)
    
