# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
browser=webdriver.Chrome()
try:
    browser.get("https://www.baidu.com")
    input=browser.find_element_by_id("kw") #定位搜索框
    input.send_keys("Python")  #键入关键字
    input.send_keys(Keys.ENTER)  #键入回车
    wait=WebDriverWait(browser,10) #等待10秒,直至返回为True
    wait.until(EC.presence_of_element_located((By.ID,"content_left")))   #如果10秒没有成功，返回until内容
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
    time.sleep(10)
finally:
    browser.close()
