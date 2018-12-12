# import http.client
# conn = http.client.HTTPSConnection("www.baidu.com")
# conn.request("GET", "/")
# r1 = conn.getresponse()
# print(r1.status, r1.reason)
'''

1、HTTPConnection函数
httplib.HTTPConnection(host[,port[,stict[,timeout]]])

这个是构造函数，表示一次与服务器之间的交互，即请求/响应
host 标识服务器主机(服务器IP或域名)
port 默认值是80
strict 模式是False，表示无法解析服务器返回的状态行时，是否抛出BadStatusLine异常
例如:
conn = httplib.HTTPConnection(“192.168.81.16”，80) 与服务器建立链接。

2、HTTPConnection.request(method,url[,body[,header]])函数
这个是向服务器发送请求

method 请求的方式，一般是post或者get，
例如：
method=”POST”或method=”Get”

url 请求的资源，请求的资源(页面或者CGI,我们这里是CGI)
例如：
url=”http://192.168.81.16/cgi-bin/python_test/test.py” 请求CGI

或者：
url=”http://192.168.81.16/python_test/test.html” 请求页面

body 需要提交到服务器的数据，可以用json，也可以用上面的格式，json需要调用json模块
headers 请求的http头headerdata = {“Host”:”192.168.81.16”}
例如:
test_data = {‘ServiceCode’:’aaaa’,’b’:’bbbbb’}
test_data_urlencode = urllib.urlencode(test_data)
requrl = “http://192.168.81.16/cgi-bin/python_test/test.py”
headerdata = {“Host”:”192.168.81.16”}
conn = httplib.HTTPConnection(“192.168.81.16”，80)
conn.request(method=”POST”,url=requrl,body=test_data_urlencode,headers = headerdata)
conn在使用完毕后，应该关闭，conn.close()

3、HTTPConnection.getresponse()函数
这个是获取http响应，返回的对象是HTTPResponse的实例。

4、HTTPResponse介绍：
HTTPResponse的属性如下：
read([amt]) 获取响应消息体，amt表示从响应流中读取指定字节的数据，没有指定时，将全部数据读出；
getheader(name[,default]) 获得响应的header，name是表示头域名，在没有头域名的时候，default用来指定返回值
getheaders() 以列表的形式获得header
例如：

date=response.getheader(‘date’);
print date
resheader=”
resheader=response.getheaders();
print resheader

列形式的响应头部信息:

[(‘content-length’, ‘295’), (‘accept-ranges’, ‘bytes’), (‘server’, ‘Apache’), (‘last-modified’, ‘Sat, 31 Mar 2012 10:07:02 GMT’), (‘connection’, ‘close’), (‘etag’, ‘“e8744-127-4bc871e4fdd80”’), (‘date’, ‘Mon, 03 Sep 2012 10:01:47 GMT’), (‘content-type’, ‘text/html’)]

date=response.getheader(‘date’);
print date

取出响应头部的date的值。
'''
#
# import http.client
#
# conn=http.client.HTTPConnection('www.baidu.com')
# conn.request('GET','/')
# body=conn.getresponse().read().decode('utf-8')
# conn.close()
# print(body)

# import http.server
# import socketserver
#
# PORT = 8000
#
# Handler = http.server.SimpleHTTPRequestHandler
#
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    每次连接到服务器时都会实例化一次，并且必须覆盖handle（）方法以实现与client的通信。
    """

    def handle(self):
        # self.request是连接到客户端的TCPsocket
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()