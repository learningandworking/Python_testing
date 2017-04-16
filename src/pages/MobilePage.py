'''
Created on Mar 23, 2017

@author: hung.dao
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.BasePage import BasePage

class MobilePage(BasePage):
    
    '''
    Page Locators and Functions of Mobile Home page.
    
    '''
    
    #Link Text location.
    SORTBY_BOX = (By.XPATH, '//*[@class="sort-by"]//*[@title="Sort By"]')

    PRODUCT_NAME_LIST = []
    ADD_CART_BUTTON = '//div[@class="product-info"]//[@title= "Add to Cart"]'
    
    #Functions
    def __init__(self, driver):
        super(MobilePage, self).__init__(driver)
    
    def get_price_homepage(self, product_name):
        #find product name.
        self.PRODUCT_NAME_LIST = self.find_all_get_attribute('//li[@class="item last"]//h2/a', "title")

        #find price
        if product_name in self.PRODUCT_NAME_LIST:
            for p in self.driver.find_elements_by_xpath(
                '//h2/a[@title="%s"]/../..//span[contains(@id, "product-price")]' %product_name):
                self.price_home = p.text
        else:
            print "There is no %s in our page, please try another one: " %product_name
        return self.price_home
    
    def add_to_cart(self):
        pass
    
    ###############################################################################################
    '''
    Page locators and Functions of Mobile Detail page
    '''
    #Locators
    PRODUCT_DETAILPRICE = '//div[@class= "product-shop"//[@class="price"]'
    PRODUCT_DETAILNAME = '//div[@class= "product-shop"//[@class="product-name"]'
    
    
    #Functions
    def go_to_detail_page(self, product_name):
        self.click_link(product_name)
        
    def get_price_detailpage(self):
        for p in self.driver.find_elements_by_xpath(
                '//div[@class="price-box"]//span[contains(@id, "product-price")]'):
            self.price_detail = p.text
            break
            
        return self.price_detail