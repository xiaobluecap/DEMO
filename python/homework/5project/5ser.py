import select
import socket

ss = socket.socket()
ss.bind(('127.0.0.1', 8799))
ss.listen()

writerlist = []
readlist = [ss]
errorlist = []
msg_dict = {}

while True:
    rlist, wlist, elist = select.select(readlist, writerlist, errorlist)

    if rlist:
        for i in rlist:
            if i is ss:
                try:
                    conn, add = i.accept()
                    writerlist.append(conn)
                except Exception:
                    continue


            else:
                try:
                    msg = i.recv(1024)
                    msg_dict[i] = msg
                    if not msg:
                        i.close()
                        readlist.remove(i)
                    else:
                        print(msg)
                        readlist.remove(i)
                        writerlist.append(i)
                except Exception:
                    i.close()
                    readlist.remove(i)
                    continue

    if wlist:
        for i in wlist:
            try:
                msg = msg_dict[i]
                i.send(msg)
                writerlist.remove(i)
                del msg_dict[i]
            except Exception:
                i.close()
                writerlist.remove(i)
