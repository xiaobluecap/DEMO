import select

import socket
from urllib import parse


class Craler():
    def __init__(self):
        self.header = "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:keep-alive\r\nUser-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36\r\n\r\n"
        self.readList = []
        self.wirterList = []
        self.errorList = []
        self.sec = select
        self.url_temp = {}

    def url_class(self):
        for i in range(114490, 114500):
            tmp_url = "http://blog.jobbole.com/{}/".format(114461)
            server = socket.socket()
            server.setblocking(False)
            try:
                server.connect(("123.206.1.112", 80))
            except:
                pass
            self.url_temp[server] = tmp_url
            self.wirterList.append(server)

    def start(self):
        self.url_class()
        while True:
            rlist, wlist, elist = self.sec.select(self.readList, self.wirterList, self.errorList)

            if wlist:
                for i in wlist:
                    host = self.url_temp[i]
                    header, host = self.format_host(host=host)
                    try:
                        i.send(header.encode())
                        self.wirterList.remove(i)
                        self.readList.append(i)
                    except:
                        i.connect(("123.206.1.112", 80))

            if rlist:
                for i in rlist:
                    msg = i.recv(1024)
                    print(msg)
                    self.readList.remove(i)

    def format_host(self, host):
        url = parse.urlparse(host)
        hostname = url.hostname
        path = url.path if url.path else '/'
        header = self.header.format(path, hostname)
        return header, host


if __name__ == '__main__':
    ss = Craler()
    ss.start()
    print('000000000000000000000000000000000000000000000000000000')
