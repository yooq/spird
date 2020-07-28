'''
单个元素
'''
#_*_coding: utf-8_*_

from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Chrome()
browser.get("http://www.taobao.com")
input_first=browser.find_element_by_id("q")
input_second=browser.find_element_by_css_selector("#q")
input_third=browser.find_element(By.ID,"q")
# print(input_first,input_second,input_first)
browser.close()

'''
多个元素
'''
#_*_coding: utf-8_*_

from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Chrome()
browser.get("http://www.taobao.com")
# 同一种find 查找两种不同的元素
lis=browser.find_element_by_css_selector("li")
lis_c=browser.find_element(By.CSS_SELECTOR,"li")
print(lis,lis_c)
browser.close()

