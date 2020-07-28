from selenium import webdriver#导入库
browser = webdriver.Chrome()#声明浏览器
url = 'https:www.taobao.com'
browser.get(url)#打开浏览器预设网址
input_first = browser.find_element_by_id('q')
input_two = browser.find_element_by_css_selector('#q')
print(input_first)
print(input_two)
