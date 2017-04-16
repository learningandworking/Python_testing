'''
Created on Mar 23, 2017

@author: hung.dao
'''

import logging
import unittest
import time
from selenium import webdriver
from pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test(unittest.TestCase):
    
    #url ='http://live.guru99.com/index.php/'
    #self.url ='http://live.guru99.com/index.php/'
    #text = 'THIS IS DEMO SITE'
    SORT_BY = '//*[@class="sort-by"]//*[@title="Sort By"]'
    Name_item = 'Name'
   
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.driver = webdriver.Firefox()
        self.home = BasePage(self.driver)
        self.url ='http://live.guru99.com/index.php/'
        self.text = 'THIS IS DEMO SITE'
    
    def setUp(self):
        logging.info("\n==================================================\n")
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)


    def tearDown(self):
        logging.info("\n==================================================\n")
        self.driver.close()


    def test_TC01_Step1(self): 
        logging.info("Test case 1 - Step 1: access_page_and_verify_text")
        self.h2tag_text = self.home.get_text_from_classname('page-title') 
        assert self.text in self.h2tag_text
        
    def test_TC01_Step2(self):
        logging.info("Test case 1 - Step 2: Verify_the_title_homepage")
        assert self.driver.title in 'Home page'

    def test_TC01_Step3to6(self):
        logging.info("Test case 1 - Step 3and4: Click on Mobile menu and verify title of Mobile page")
        # Neu ko co try, finally ==> se co loi:  maximum recursive-error-runtimeerror-maximum-recursion-depth-exceeded
        # lien quan den "title", co the la do, page chay qua nhanh, nen can thoi gian on dinh lai assert title.
        
        try:
            self.home.click_link('Mobile')
            self.element = WebDriverWait(self.driver, 10).until(EC.title_is('Mobile'))
        finally:
            print "The title of Page is Mobile, that is: ", self.element
            self.mobile_url = self.driver.current_url
            print "The current URL is: ", self.mobile_url
        
        print('-------------------------------------------------------------------------------------')    
        logging.info("Test case 1 - Step 5and6: Click SortBy and verify all product are sorted")        
        #Choose "Name" from dropdown-box.
        self.home.choose_item_dropdown(self.SORT_BY, self.Name_item)


if __name__ == "__main__":
    unittest.main()
    
    
# a test case should have prefix "text_", if not cannot run the test
# Note: dung self.* cho moi bien va moi functions khi tao ra, khai bao
# dung self.h2tag_text, thay vi h2tag_text, neu ko bao loi TEST ko co attribute la h2_tag_text
#dung __init__ va super, de co the tao instance object cua class HOme(self.home) , sau do reuse lai trong nhieu def