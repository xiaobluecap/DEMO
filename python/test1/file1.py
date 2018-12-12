'''

#GET请求
# import urllib.request
#
#
# response=urllib.request.urlopen('http://www.zhihu.com')
# html=response.readlines()
# for i in html:
#     print(i)



# import urllib.request
#
# req=urllib.request.Request('http://www.zhihu.com')
# thml=urllib.request.urlopen(req)
# data=thml.read()
# print(data)

#POST请求
# import urllib
# import urllib.parse
# import urllib.request
# url='httP://www.zhihu.com'
# postdata={
#     'username':'qiye',
#     'password':'qiye_pass'
# }
#
# data=urllib.parse.urlencode(postdata).encode('ascii')
# #请求体
# req=urllib.request.Request(url,data)
# html=urllib.request.urlopen(req)
# print(html.read().decode('utf-8'))




#请求头header处理
# import urllib
# import urllib.parse
# import urllib.request
#
# url='http://www.zhihu.com'
# user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
# redere='https://blog.csdn.net/duxu24/article/details/77414298'
# postdata={
#     'username':'qiye',
#     'password':'qiye_pass'
# }
# # header={
# #     'user_agent':user_agent,'refere':redere
# # }
# data=urllib.parse.urlencode(postdata).encode('ascii')
# # req=urllib.request.Request(url,data,header)
# # html=urllib.request.urlopen(req)
# # print(html.read().decode('utf-8'))
# #add.header
# req=urllib.request(url)
# req.add_header('user_agent',user_agent)
# req.add_header('refere',redere)
# req.add_data(data)
# html=urllib.request.urlopen(req)
# print(html.read().decode('utf-8'))





#使用add_header方法添加请求头信息
# import urllib
# import urllib.parse
# import urllib.request
#
#
# url='http://www.bilibili.com/'
# user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
# redere='https://blog.csdn.net/duxu24/article/details/77414298'
# postdata={'usrname':'17311683482',
#           'password':'pc.ppdemo'}
# data=urllib.parse.urlencode(postdata).encode('ascii')
# header={'user_agent':user_agent,'redere':redere}
# req=urllib.request.Request(url,data,header)
# html=urllib.request.urlopen(req)
# print(html.read().decode('utf-8'))



#cookie处理
# import urllib.request
# import http.cookiejar
#
# url='http://zhihu.com'
#
# cookie=http.cookiejar.CookieJar()#声明一个CookieJar对象实例来保存cookie
#
# hander=urllib.request.HTTPCookieProcessor(cookie)#使用HTTPCookieProcessor对象来创建一个cookie处理器
#
# opener=urllib.request.build_opener(hander)#通过hander来构建opener
#
# response=opener.open(url)#与urlopen方法一样，可以传入request
#
# for item in cookie:
#     print('name='+item.name)
#     print('value='+item.value)

# #proxy设置代理
# from urllib.error import URLError
# from urllib.request import ProxyHandler,build_opener
#
# proxy='127.0.0.1:9934'
# proxy_hander=ProxyHandler({
#     'http':'http://'+proxy,
#     'https':'https://'+proxy
# })
# opener=build_opener(proxy_hander)
# try:
#     response=opener.open('http://httpbin.org/get')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

import requests
r=requests.get('http://seputu.com/')
print(r.text)



# import requests,chardet
# r=requests.get('http://www.zhihu.com')
# print(chardet.detect(r.content))
# r.encoding=chardet.detect(r.content)['encoding']
# print(r.text)

# import requests
# user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
# headers={'user_agent':user_agent}
# #r=requests.get('http://seputu.com/',headers=headers)
# r=requests.get('http://seputu.com/',headers=headers)
# print(r.content)

'''
#beautifulsoup
from bs4 import BeautifulSoup
import lxml
html_str='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

soup=BeautifulSoup(html_str,'lxml',from_encoding='utf-8')
# print(soup.frameset)
# print(soup.name)
# soup.title.name='pp'
# print(soup.pp.name)
# print(soup.p.string)
# print(len(soup.head.contents))
# print(soup.head.contents[1])

# for child in soup.head.children:
#     print(child)

print(soup.title.parent)