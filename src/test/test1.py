'''
Created on Apr 3, 2017

@author: hung.dao
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.MobilePage import MobilePage



driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://live.guru99.com/index.php/mobile/sony-xperia.html')
m = MobilePage(driver)

a = m.get_price_detailpage()
print a

driver.close()
'''
PRODUCT_NAME_LIST = []
product_name = "Sony Xperia"
a = driver.find_elements_by_xpath('//div[@class="price-box"]//span[contains(@id, "product-price")]')
#(By.XPATH, '//h2[@class="product-name"]//title')

el = []
for i in a:
    print i.text


#for i in driver.find_elements_by_xpath('//*[@title= "Samsung Galaxy"]//div[@id = "old-price-"][contains(., "$")]'):
#print a

x = "Samsung Galaxy"
b = driver.find_elements_by_xpath('//h2/a[@title="%s"]/../..//span[contains(@id, "product-price")]' %product_name)

for i in b:
    print i.text
'''