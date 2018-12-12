# import requests
#
# user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
# headers={'user_agent':user_agent}
# r=requests.get('http://www.seputu.com/',headers=headers)
# # print(r.text)
# from bs4 import BeautifulSoup
# import lxml
#
# soup=BeautifulSoup(r.text,'lxml',from_encoding='utf-8')
# for mulu in soup.find_all(class_='mulu'):
#     h2=mulu.find('h2')
#     if h2!=None:
#         h2_title=h2.string#获取标题
#         # print(h2_title)
#         for a in mulu.find(class_='box').find_all('a'):#获取所有a标记中url和章节内容
#             # print(a)
#             href=a.get('href')
#             box_title=a.get('title')
#             print(href,box_title)


import requests

user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
headers={'user_agent':user_agent}
r=requests.get('http://www.seputu.com/',headers=headers)
# print(r.text)
from bs4 import BeautifulSoup
import json

soup=BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')
content=[]
