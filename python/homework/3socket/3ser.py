import socket


class Ser(object):

    def __init__(self, ip='127.0.0.1', port=8899, url=r"D:\pycharm\data\DemoA\one.txt"):
        self.ip = ip
        self.port = port
        self.url = url
        self.address = (self.ip, self.port)
        self.server = socket.socket()
        self.server.bind(self.address)
        self.server.listen()

    def open_file(self):
        with open(self.url, 'rb')as task:
            date = task.read(1024)
            #print(date)
            return date

    def send_file(self, conn):
        date = self.open_file()
        date=str(date)
        conn.send(date.encode())

    def start(self):
        conn, add = self.server.accept()
        self.send_file(conn)


if __name__ == '__main__':
    ser = Ser()
    ser.start()
