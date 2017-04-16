'''
Created on Mar 27, 2017

@author: hung.dao
'''
import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    
    
        
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()