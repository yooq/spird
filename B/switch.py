import selenium
from selenium import webdriver
import time


'''网页切换'''
driver =webdriver.Chrome()
url ='https://www.douban.com/'
driver.get(url)
# driver.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[2]/a').click()
# time.sleep(10)
# windows = driver.window_handles
# driver.switch_to_window(windows[0]) #窗口切换
# time.sleep(1)
# driver.back()
# driver.forward()
# time.sleep(1)
# driver.quit()



'''嵌套切换实现自动登录'''
driver.switch_to_frame(0)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
time.sleep(3)
# driver.close()
driver.find_element_by_xpath('//*[@id="username"]').send_keys('18229926519')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('569569lmx')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
