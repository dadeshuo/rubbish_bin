#!/usr/bin/python3


from lxml import etree
import time,os,sys
from collections import defaultdict

class CTS_module:
    def __init__(self,element):
        self.error_dict=defaultdict(list)
        self.element=element
        self.module_name=self.element.get('name')
        self.abi=self.element.get('abi')
    
    def add_err(self,test):
        self.error_dict[test.testcase].append(test)

class CTS_error:
    def __init__(self,element):
        self.element=element
        self.testcase=self.element.getparent().get('name')
        self.name=self.element.get('name')
        self.message=self.element[0].get('message').replace('\t','')
        self.stacktrack=self.element[0][0].text.replace('\t','')


def find_error(tree):
    for Module in tree.getroot():
        if Module.tag=='Module':
            module_error=CTS_module(Module)
            for item in etree.XPath(r".//Test[@result='fail']")(Module):
                module_error.add_err(CTS_error(item))
            if len(module_error.error_dict)!=0:
                #print(module_error.error_dict)
                yield module_error

           
def s_output(output_path,err_list):
    with open(output_path+r'/s_output.txt', mode='w')as err_result:
        err_result.write('\n'*3)
        for item in err_list:
            err_result.write('Module:  '+item.module_name+'     '+'abi:  '+item.abi+'\n'*2)
            for key,value in item.error_dict.items():
                err_result.write(key+':'+'\n'*2)
                for error in value:
                    err_result.write('-- '+error.name+'\n')
                err_result.write('\n')
            err_result.write('\n'*2+'-'*20+'\n'*2)

def m_output(output_path,err_list):
    with open(output_path+r'/m_output.txt', mode='w')as err_result:
        err_result.write('\n'*3)
        for item in err_list:
            err_result.write('Module:  '+item.module_name+'     '+'abi:  '+item.abi+'\n'*2)
            for key,value in item.error_dict.items():
                err_result.write(key+':'+'\n'*2)
                for error in value:
                    err_result.write('-- '+error.name+':\n')
                    err_result.write(error.message+'\n'*3)
                err_result.write('\n')
            err_result.write('\n'*2+'-'*20+'\n'*2)

def l_output(output_path,err_list):
    with open(output_path+r'/l_output.txt', mode='w')as err_result:
        err_result.write('\n'*3)
        for item in err_list:
            err_result.write('Module:  '+item.module_name+'     '+'abi:  '+item.abi+'\n'*2)
            for key,value in item.error_dict.items():
                err_result.write(key+':'+'\n'*2)
                for error in value:
                    err_result.write('-- '+error.name+':\n')
                    err_result.write(error.message+'\n')
                    err_result.write('#'*20+'\n'+error.stacktrack+'\n'+'#'*20+'\n'*2)
                err_result.write('\n')
            err_result.write('\n'*2+'-'*20+'\n'*2)

def main(org):
    tree = etree.parse(org)
    err_list=list(find_error(tree))
    output_path=os.path.abspath(os.path.dirname(org))
    s_output(output_path,err_list)
    m_output(output_path,err_list)    
    l_output(output_path,err_list)
    print('search finish')



if __name__=='__main__':
    org=sys.argv[1]
    main(org)

