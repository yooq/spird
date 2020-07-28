import requests
from bs4 import BeautifulSoup as bt
response = requests.get('https://www.autohome.com.cn/news/')
response.encoding='gbk'
'''
text是现成的字符串，.content还要编码
text一般用于返回的文本
content的一般用于对返回的其他数据类型

'''
# print(response.text)
obj = bt(response.text,'html.parser')

# find_test = obj.find('script')  #只能找到第一个匹配成功的标签
# print(type(find_test)) #<class 'bs4.element.Tag'>
# find_test_ = obj.find_all('script') #找到所有匹配成功的标签
# print(type(find_test_),len(find_test_))  #<class 'bs4.element.ResultSet'> 14

find_id = obj.find(id='auto-channel-lazyload-article')
find_li = find_id.find_all('li')

for l in find_li:
    print('======'*20)
    title = l.find('h3')
    if title is None:
        continue
    title = title.text
    summary = l.find('p').text

    label_dict = l.find('a').attrs #所有标签的dict
    content_url = label_dict['href'] #内容在此处 等价于 l.find('a').get('href') 等价于 l.find('a').attrs['href']
    content_url = 'http:'+content_url

    image = l.find('img').attrs['src']
    image = 'http:'+image

    print(title,image,summary,content_url)
