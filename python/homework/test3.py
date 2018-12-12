from bs4 import BeautifulSoup
import requests,queue





def DG(url):
    list1=[]
    list1.append(url)
    list2=queue.Queue()
    while list1!=0:
        url1=list1.pop()
        r = requests.get(url1)
        html = r.text
        print(html)
        soup = BeautifulSoup(html)
        dom2 = soup.find_all('a', class_='archive-title')
        dom1 = soup.find_all('a', class_='page-numbers')
        for i in dom2:
            list2.put(i.attrs['href'])
        for i in dom1:
            if i.attrs['href'] not in list1:
                DG(i.attrs['href'])

url=' http://blog.jobbole.com/all-posts/'
DG(url)




# class pac:
#     def __init__(self):
#         self.queue1=queue.Queue()
#         self.queue2=queue.Queue()
#         self.first_url=' http://blog.jobbole.com/all-posts/'
#         self.queue1.put(self.first_url)
#         self.list2=[]
#
#
#
#     def get_html(self,url):
#         r = requests.get(url)
#         html = r.text
#         return html
#
#
#     def hhtml(self,html):
#         soup = BeautifulSoup(html)
#         dom2 = soup.find_all('a', class_='archive-title')
#         dom1 = soup.find_all('a', class_='page-numbers')
#         list_art=[]
#         list_page=[]
#         for i in dom1:
#             if i not in self.list2:
#                 list_page.append(i.attrs['href'])
#         for i in dom2:
#             list_art.append(i.attrs['href'])
#
#         return list_art,list_page
#
#
#
#     def indexhtml(self):
#         print('4')
#         while True:
#             url=self.queue1.get()
#             html=self.get_html(url)
#             list1,list2=self.hhtml(html)
#             for i in list1:
#                 self.queue2.put(i)
#             for i in list2:
#                 self.queue1.put(i)
#
#
#
#
#
#     def arthtml(self):
#         print('5')
#         while True:
#             url=self.queue2.get()
#             html = self.get_html(url)
#             print('queue1的长度{}queue2的长度{}'.format(self.queue1.qsize(), self.queue2.qsize()))
#
#
#
#     def start(self):
#         print('1')
#         t1=threading.Thread(target=self.indexhtml)
#         t2=threading.Thread(target=self.arthtml)
#         print('2')
#         t1.start()
#         t2.start()
#         print('3')
#         t1.join()
#         t2.join()
#
#
# if __name__=="__main__":
#     pc=pac()
#     pc.start()
#
