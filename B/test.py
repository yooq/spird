import selenium
from selenium import webdriver
import time
if __name__ == '__main__':
    '''
    1.创建浏览器对象 from selenium import webdriver
        
    '''
    dirver = webdriver.Chrome()

    '''
    请求页面
    '''
    url = 'https://www.baidu.com'
    dirver.get(url=url)

    '''
    点击和输入
    '''
    inputs = dirver.find_element_by_id('kw')
    inputs.send_keys('sadsafsad')
    '''点击回车'''
    # 方法一
    # from selenium.webdriver.common.keys import Keys
    # inputs.send_keys(Keys.ENTER)

    #方法二
    dirver.find_element_by_id('su').click()

    '''保存截图'''
    time.sleep(5)
    dirver.save_screenshot('sadsafsad.png')

    '''获取页面数据'''
    # print(dirver.page_source)

    '''元素定位'''
    




    time.sleep(3)
    dirver.close() #关闭页面
    dirver.quit()  #关闭所有页面



