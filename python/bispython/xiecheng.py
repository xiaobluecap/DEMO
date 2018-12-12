# '''
# import gevent,socket
#
# urls = ['www.baidu.com', 'www.gevent.org', 'www.python.org']
# jobs=[gevent.spawn(socket.gethostbyname,url) for url in urls]
# gevent.joinall(jobs,timeout=5)
# for job in jobs:
#     print(job.value)
# '''
#
# from gevent import monkey;monkey.patch_socket()
# import gevent
# import socket
# urls = ['www.baidu.com', 'www.gevent.org', 'www.python.org']
# jobs=[gevent.spawn(socket.gethostbyname,url) for url in urls]
# gevent.joinall(jobs,timeout=5)
# for job in jobs:
#     print(job.value)



