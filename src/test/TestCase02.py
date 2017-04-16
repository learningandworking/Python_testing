'''
Created on Apr 3, 2017

@author: hung.dao
'''
import logging
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test.BaseTest_ver2 import BaseTest
from pages.MobilePage import MobilePage
from pages.BasePage import BasePage
from nose.tools import assert_equal
from time import sleep


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class Test(BaseTest):
    
    url ='http://live.guru99.com/index.php'
    product_name = "Sony Xperia"
    
    
    @classmethod
    def setUpClass(cls):
        logging.info('--------Start Setup--------- ')
        super(Test, cls).setUpClass() # call parent method
        cls.driver.get(cls.url)
        cls.home = BasePage(cls.driver)
        cls.mobile = MobilePage(cls.driver) 
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()    

    def test_TC02_Step1to3(self):
        
        logging.info('Step1: Access to WebPage\n')
        
        logging.info('Step2: Click on Mobile menu\n')
        
        #################
        self.home.click_link('Mobile')
        self.element = WebDriverWait(self.driver, 10).until(EC.title_is('Mobile'))
        logging.info("Step3 - The Home Price of %s is: %s" %(self.product_name, 
                                                        self.mobile.get_price_homepage(self.product_name)))
        
        #################
        logging.info("Step4: Access to the detail page of %s" %self.product_name)
        self.mobile.go_to_detail_page(self.product_name)
        self.element = WebDriverWait(self.driver, 15).until(EC.title_is(self.product_name + " - Mobile"))
        logging.info("Step3 - The Detail Price is %s: " %self.mobile.get_price_detailpage)
        
        if self.mobile.get_price_detailpage == self.mobile.get_price_homepage:
            print "Passed"
        else:
            print "Failed"
        

if __name__ == "__main__":
    unittest.main(verbosity=2)