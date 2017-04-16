'''
Created on Mar 23, 2017

@author: hung.dao
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import unittest


class BasePage(object):
    '''
    classdocs
    '''

    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver
    
    def click_link(self, link):
        el = self.driver.find_element_by_link_text(link)
        el.click()
        
    def get_text_from_classname(self, class_name):# not text()
        return self.driver.find_element_by_class_name(class_name).text
    
    def get_text_from_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath).text
    
    def assert_title(self, title):
        self.assert_title(title)
    
    def click_xpath(self, xpath):
        el = self.driver.find_element_by_xpath(xpath)
        el.click()
    
    def find_all_get_attribute(self, xpath, var_attri):
        list_el = []
        for i in self.driver.find_elements_by_xpath(xpath):
            list_el.append(i.get_attribute(var_attri))
        return list_el
        
    def choose_item_dropdown(self, xpath_drop, item):
        self.select = Select(self.driver.find_element_by_xpath(xpath_drop))
        
        # select by visible text
        self.select.select_by_visible_text(item)

        # select by value 
        #select.select_by_value('1')
        
        
    
        
        