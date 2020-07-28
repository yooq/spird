import requests
from bs4 import BeautifulSoup as bt

response = requests.get('https://github.com/login')


obj = bt(response.text,'html.parser')

# 获取token 
login = obj.find(name='input',attrs={'name':'authenticity_token'}).get('value')
print(login)

