'''
Created on Mar 27, 2017

@author: hung.dao
'''

class test1(object):
    '''
    classdocs
    '''


    def add_num(self, num1=5, num2=6):
        return num1 + num2
    
    def display_num(self, num3=1, num4=4):
        print "num 1: ", num3
        print "num 2: ", num4

        
class test2(test1):

    def hien_num(self):
        pass
        
    def print_funtion(self):
        super(test1, self).display_num()
        print "hello"   

cls_test2 = test2()
cls_test2.print_funtion()