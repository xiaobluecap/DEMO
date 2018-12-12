# #! /usr/bin/env python
# # -*- coding:utf-8 -*-
# # Author: "Zing-p"
# # Date: 2017/5/12
#
#
# def consumer(name):
#     print("要开始啃骨头了...")
#     while True:
#         print("\033[31;1m[consumer] %s\033[0m " % name)
#         bone = yield
#         print("[%s] 正在啃骨头 %s" % (name, bone))
#
#
# def producer(obj1, obj2):
#     obj1.send(None)    # 启动obj1这个生成器,第一次必须用None  <==> obj1.__next__()
#     obj2.send(None)    # 启动obj2这个生成器,第一次必须用None  <==> obj2.__next__()
#     n = 0
#     while n < 5:
#         n += 1
#         print("\033[32;1m[producer]\033[0m 正在生产骨头 %s" % n)
#         obj1.send(n)
#         obj2.send(n)
#
#
# if __name__ == '__main__':
#     con1 = consumer("消费者A")
#     con2 = consumer("消费者B")
#     producer(con1, con2)





# import time
#
# def condumer():
#     r=''
#     while True:
#         n=yield r
#         if not n:
#             return
#         print('[condumer]Consuming %s...'%n)
#         time.sleep(1)
#         r='200 OK'
#
# def produce(c):
#     c.send(None)
#     n=0
#     while n<5:
#         n+=1
#         print('[PRODUCE]producing %s'%n)
#         r=c.send(n)
#         print('[PRODUCE]consumer return %s'%n)
#     c.close()
#
# if __name__=="__main__":
#     c=condumer()
#     produce(c)
#
# import gevent
#
# def test1():
#     print(12)
#     gevent.sleep(0)
#     print(34)
#
# def test2():
#     print(56)
#     gevent.sleep(0)
#     print(78)
#
# gevent.joinall([
#     gevent.spawn(test1),
#     gevent.spawn(test2),
# ])


# def count(n):
#     x=0
#     while x<n:
#         yield x
#         x+=1
#
# for i in count(5):
#     print(i)

# def consumer():
#     last=''
#     while True:
#         receival=yield last
#         if receival is not None:
#             print('Consumer %s'%(receival))
#             last=receival
#
# def producer(gen,n):
#     gen.next()
#     x=0
#     while x<n:
#         x+=1
#         print('Produce %s'%x)
#         last=gen.send(x)
#     gen.close()
# gen=consumer()
# producer(gen,5)


from greenlet import greenlet

def test1():
    print(12)
    try:
        gr2.switch()
    except NameError:
        print(90)
    print(34)

def test2():
    print(56)
    raise NameError
gr1=greenlet(test1)
gr2=greenlet(test2,gr1)
gr1.switch()


from greenlet import greenlet
def consumer():
    last=''
    while True:
        receival=pro.swith(last)
        if receival is not None:
            print('Cousumer %s'%(receival))
            last=receival


def producer(n):
    con.switch()
    x=0
    while x<n:
        x+=1
        print('Produce %s'%x)
        last=con.switch(x)


pro=greenlet(producer)
con=greenlet(consumer)
pro.switch(5)




























