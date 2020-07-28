from selenium import webdriver
import time

'''网页切换'''
driver =webdriver.Chrome()
url ='https://mp.weixin.qq.com/'
driver.get(url)


driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[2]/a').click()

driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[1]/div/span/input').send_keys('990250040@qq.com')
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[2]/div/span/input').send_keys('zhangwei9578')
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[3]/label/i').click()
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[4]/a').click()
