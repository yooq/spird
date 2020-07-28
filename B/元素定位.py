import selenium
from selenium import webdriver
import time

driver =webdriver.Chrome()
url ='https://www.douban.com/'
driver.get(url)

r1 = driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div')
print(r1.text)
r2 = driver.find_element_by_link_text('下载豆瓣 App')  #内容 模糊查询定位
print(r2.get_attribute('href'))
print(r2.text)
r2.find_element_by_class_name()

driver.close()
