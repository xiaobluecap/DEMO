import socket,queue
from concurrent.futures import ThreadPoolExecutor





class Server(object):
    def __init__(self,ip='127.0.0.1',port=33667):
        self.ip=ip
        self.port=port
        self.address=(ip,port)
        self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind(self.address)
        self.server.listen(9)
        self.pools=ThreadPoolExecutor(23)
        self.couns=list()
        self.queue=queue.Queue()

    def recv_msg(self,conn,add):
        while True:
            # conn,add=self.server.accept()
            msg=conn.recv(1024)
            if (not msg) or (len(msg) == 0):
                self.close_conn(conn,add)
            self.queue.put((msg,conn))
            for conn in self.couns:
                conn.send("ip为{},说:{}".format(add, msg.decode()).encode())
            print('ip为{}，的消息{}'.format(add,msg.decode('utf8')))





    def send_msg(self):
        while True:
            msg,add=self.queue.get()
            ip,port=add
            for conn in self.couns:
                conn.send("ip为{},port为{},说:{}".format(ip, port, msg.decode()).encode())
                # try:
                #     conn.send("ip为{},port为{},说:{}".format(ip, port, msg.decode()).encode())
                # except Exception:
                #     self.close_conn(conn, add)

    def start(self):
        self.pools.submit(self.send_msg)
        while True:
            conn,add=self.server.accept()
            self.pools.submit(self.recv_msg,conn,add)
            self.couns.append(conn)


    def close_conn(self,conn,add):
        conn.close()
        self.couns.remove(conn)
        msg='ip为{}退出'.format(add)
        self.queue.put((msg,conn))



if __name__ =='__main__':
    ser=Server()
    ser.start()