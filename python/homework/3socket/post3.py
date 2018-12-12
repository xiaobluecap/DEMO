






header='''
        POST www.zhihu.com HTTP/1.1
        Accept: application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*
        Referer: http://localhost:8080/02_WEB_HTTP/form.html
        Accept-Language: zh-CN,en-US;q=0.7,ko-KR;q=0.3
        User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3)
        Content-Type: application/x-www-form-urlencoded
        Accept-Encoding: gzip, deflate
        Host: localhost:8080
        Content-Length: 30
        Connection: Keep-Alive
        Cache-Control: no-cache 
         
        username=admin&password=123123
        '''

import socket


post_str = 'POST %s HTTP/1.1\r\nHost: %s\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36\r\n\r\n%s\r\n\r\n'

server=socket.socket()
server.connect(('118.89.204.100',80))
server.send(post_str.encode())
date=server.recv(1024)
print(date)




'''
get_str = 'GET %s HTTP/1.1\r\nHost: %s\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36\r\nAccept: */*\r\n\r\n'
post_str = 'POST %s HTTP/1.1\r\nHost: %s\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36\r\n\r\n%s\r\n\r\n'


def get():
    sock=socket.socket()
    sock.connect(('118.89.204.100',80))
    sock.send(get_str.encode())
    
    response = ''    
    temp = sock.recv(4096)
    while temp:
        temp = sock.recv(4096)
        response += temp

    return response


if __name__=="__main__":
    get()
'''
