import socket,queue
from concurrent.futures import ThreadPoolExecutor




class Ser(object):


    def __init__(self,ip='127.0.0.1',port=7799):
        self.ip=ip
        self.port=port
        self.address=(self.ip,self.port)
        self.server=socket.socket()
        self.server.bind(self.address)
        self.server.listen(34)
        self.conns=list()
        self.queue=queue.Queue()
        self.atsk=ThreadPoolExecutor(8)


    def recv_msg(self,conn,add):
        while True:
            msg=conn.recv(1024)
            if (not msg) or len(msg)==0:
                self.close_conn(conn,add)
            self.queue.put(msg,add)
            print('收到ip为{}的消息{}'.format(add, msg.decode()))

    def send_msg(self):
        while True:
            msg, add = self.queue.get()
            for conn in self.conns:
                # conn.send(('ip是{}的发送了{}'.format(add, msg)).encode('utf8'))
                try:
                    conn.send('ip是{}的发送了{}'.format(add,msg).encode('utf8'))
                except Exception:
                    self.close_conn(conn,add)

    def close_conn(self,conn,add):
        conn.close()
        self.conns.remove(conn)
        msg='ip为{}断开了连接'.format(conn).encode('utf8')
        self.queue.put(msg,add)

    def start(self):
        self.atsk.submit(self.send_msg)
        while True:
            conn, add = self.server.accept()
            self.atsk.submit(self.recv_msg,conn,add)
            self.conns.append(conn)

if __name__=="__main__":
    ser=Ser()
    ser.start()


'''
    def recv_msg(self, conn, addr):

        while True:
            msg = conn.recv(1024)
            if (not msg) or (len(msg) == 0):
                self.remove_conn(conn,addr)
            self.msg_queue.put((msg, addr))
            print('收到ip为{}的消息{}'.format(addr, msg.decode()))


    def remove_conn(self,conn,addr):
        conn.close()
        self.conns.remove(conn)
        msg = '我已经退出聊天'.encode()
        self.msg_queue.put((msg, addr))

    def is_black(self, addr):
        """
        判断黑名单用户
        :return:
        """
        ip, port = addr
        if ip in self.black_list:
            return True
        else:
            return False


if __name__ == "__main__":
    ss = Server()
    ss.start()

'''