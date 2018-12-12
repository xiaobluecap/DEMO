import select

import socket

server = socket.socket()
server.bind(('127.0.0.1', 8899))
server.listen(5)

readList = [server]
witerList = []
errorList = []
msg_dict = {}

while True:
    rlist, wlist, elist = select.select(readList, witerList, errorList)

    if rlist:
        for i in rlist:
            if i is server:
                try:
                    conn, add = i.accept()
                    readList.append(conn)
                except Exception:
                    continue


            else:
                try:
                    msg = i.recv(1024)
                    msg_dict[i] = msg
                    if not msg:
                        i.close()
                        readList.remove(i)
                        continue
                    else:
                        print(msg)
                        readList.remove(i)
                        witerList.append(i)
                except Exception:
                    i.close()
                    readList.remove(i)
                    continue

    if wlist:
        for i in wlist:
            try:
                msg = msg_dict[i]
                i.send(msg)
                witerList.remove(i)
                del msg_dict[i]
            except Exception:
                i.close()
                witerList.remove(i)
                continue
