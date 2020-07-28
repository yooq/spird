#_*_coding: utf-8_*_
from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get("https://www.taobao.com")
input=browser.find_element_by_id("q")
input.send_keys("iPhone")
time.sleep(10)
input.clear()
input.send_keys("iPad")
button=browser.find_element_by_class_name("btn-search") #点击搜索
button.click()
time.sleep(10)
browser.close()
