from bs4 import BeautifulSoup
import requests,queue








r = requests.get(' http://blog.jobbole.com/all-posts/')
html = r.text

soup = BeautifulSoup(html)
dom2 = soup.find_all('a', class_='archive-title')
dom1 = soup.find_all('a', class_='page-numbers')
for i in dom2:
    print(i.attrs['href'])
