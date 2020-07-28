#_*_coding: utf-8_*_

from selenium import webdriver
browser=webdriver.Chrome()
browser.get("http://www.lvmama.com")
# print(browser.page_source)

print(browser.name) #chrome
print(browser.current_url) #http://www.lvmama.com/
print(browser.title) #【驴妈妈旅游】_景点门票_自由行_跟团游_国内游_出境游_酒店_机票
print(browser.mobile) #<selenium.webdriver.remote.mobile.Mobile object at 0x0000000002F6DBE0>
browser.close()
