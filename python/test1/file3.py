from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
# print(soup.prettify())
# #print(soup.text)
# print(soup.name)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.attrs)
# print(soup.a.string)

# print(soup.head.contents)
# print(soup.head.children)
# print(soup.a)
#
# print(soup.a.next_sibling)

# print(soup.p.prev_sibling)
# print(soup.head.next_element)
#print(soup.find_all('a'))
# print(soup.find_all(text='elsie'))



# import json
# str=[{'username':'pp','age':44},(2,3),2]
# json_str=json.dumps(str,ensure_ascii=False)
# # print(json_str)
# # with open('oo.txt','w')as f:
# #     json.dump(str,fp=f,ensure_ascii=False)
# new_str=json.loads(json_str)
# print(new_str)
# with open('oo.txt','rb')as d:
#     print(json.load(d))