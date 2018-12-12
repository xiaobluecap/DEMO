# import requests
# r=requests.get('http://www.baidu.com')
# print(r.content)



import urllib.request


resquest=urllib.request.urlopen('http://www.baidu.com')
html=resquest.read()
print(html)