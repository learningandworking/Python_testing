'''
Created on Mar 23, 2017

@author: hung.dao
'''

import logging
import unittest
from pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test.BaseTest_ver2 import BaseTest


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class Test(BaseTest):

    SORT_BY = '//*[@class="sort-by"]//*[@title="Sort By"]'
    Name_item = 'Name'
    url ='http://live.guru99.com/index.php/'
    text = 'THIS IS DEMO SITE'
    
    @classmethod
    def setUpClass(cls):
        logging.info('--------Start Setup--------- ')
        super(Test, cls).setUpClass() # call parent method
        cls.driver.get(cls.url)
        cls.home = BasePage(cls.driver) 
    
    
    def test_TC01_Step1(self): 
        self.h2tag_text = self.home.get_text_from_classname('page-title') 
        assert self.text in self.h2tag_text
        
    def test_TC01_Step2(self):
        logging.info("Checking title in Home Page")
        logging.info("Title is : %s" % self.driver.title)
        assert self.driver.title in 'Home page'
        
 
    def test_TC01_Step3to6(self):
        logging.info("Test case 1 - Step 3 and 4: Click on Mobile menu and verify title of Mobile page")
        # Neu ko co try, finally ==> se co loi:  maximum recursive-error-runtimeerror-maximum-recursion-depth-exceeded
        # lien quan den "title", co the la do, page chay qua nhanh, nen can thoi gian on dinh lai assert title.
        
        try:
            self.home.click_link('Mobile')
            self.element = WebDriverWait(self.driver, 10).until(EC.title_is('Mobile'))
        finally:
            pass
        
        logging.info("Test case 1 - Step 5and6: Click SortBy and verify all product are sorted")
        self.home.choose_item_dropdown(self.SORT_BY, self.Name_item)


if __name__ == "__main__":
    unittest.main(verbosity=2)
    
    
# a test case should have prefix "text_", if not cannot run the test
# Note: dung self.* cho moi bien va moi functions khi tao ra, khai bao
# dung self.h2tag_text, thay vi h2tag_text, neu ko bao loi TEST ko co attribute la h2_tag_text
#dung __init__ va super, de co the tao instance object cua class HOme(self.home) , sau do reuse lai trong nhieu def