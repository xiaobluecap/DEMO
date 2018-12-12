# import multiprocessing,time
#
# class ClockProcess(multiprocessing.Process):
#     def __init__(self,interval):
#         multiprocessing.Process.__init__(self)
#         self.interval=interval
#
#
#     def run(self):
#         n=5
#         while n>0:
#             print('当前时间：{0}'.format(time.ctime()))
#             time.sleep(self.interval)
#             n-=1
#
# if __name__=='__main__':
#     p=ClockProcess(6)
#     p.start()



import multiprocessing
import time

class myProcess(multiprocessing.Process):
    def __init__(self,interval):
        multiprocessing.Process.__init__(self)
        self.interval=interval
    def run(self):
        n=5
        while n>0:
            print('当前时间：{0}'.format(time.ctime()))
            time.sleep(self.interval)
            n-=1


if __name__=='__main__':
    p=myProcess(8)
    p.start()



















import multiprocessing,os,time,random
from multiprocessing import Pool,Queue


def run(name):
    print('进程的名称：{0} ；进程的PID: {1} '.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('进程 {0} 运行了 {1} 秒'.format(name, (end - start)))


#进程间的通信：
def write(p):
    print('写进程的pid{0}'.format(os.getpid()))
    for value in [1111,2222,3333]:
        print('写进Queue{0}'.format(value))
        p.put(value)
        time.sleep(random.random())

def read(p):
    print('读进程的pid{0}'.format(os.getpid()))
    while True:
        value=p.get(True)
        print('从deque中读取的数据{0}'.format(value))

# if __name__=='__main__':
#     p=Queue()
#     pw=multiprocessing.Process(target=write,args=(p,))
#     pr=multiprocessing.Process(target=read,args=(p,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()


number=99
def addnum(i):
    global number
    number=number+i
    print(number)

# if __name__=='__main__':
#     p1=multiprocessing.Process(target=addnum,args=(5,))
#     p1.start()
#     p1.join()
#     p2=multiprocessing.Process(target=addnum,args=(8,))
#     p2.start()
#     p2.join()
#     print(number)

from multiprocessing import Process, Lock


# def func( i):
#     #lock.acquire()  # 加锁
#     with lock:
#         print('hello world', i)
#
#     #lock.release()  # 释放锁
#
#
# if __name__ == '__main__':
#
#     #lock = Lock()  # 初始化或者叫生成锁
#
#     for num in range(10):
#         Process(target=func, args=(num,)).start()
def addd(number,value,lock):
    for i in range(6):
        number+=value
        time.sleep(1)
        print('{0}{1}'.format(value,number))

if __name__=="__main__":
    lock=Lock()
    number=0
    p1 = multiprocessing.Process(target=addd, args=(number, 1, lock))
    p2 = multiprocessing.Process(target=addd, args=(number, 3, lock))
    p1.start()
    p2.start()



















class CloclProcess(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)

    def run(self):
        n=9
        while n>0:
            print(n,os.getpid())

            n-=1

# if __name__=="__main__":
#     p=CloclProcess()
#     p.start()


class ClockP1(multiprocessing.Process):
    def __init__(self,interval):
        multiprocessing.Process.__init__(self)
        self.interval=interval

    def run(self):
        print('1111111111111111{0}'.format(time.ctime()))
        time.sleep(self.interval)
        print('2222222222222222222',os.getpid())


# if __name__=='__main__':
#     p=ClockP1(4)
#     p.daemon=True
#     p.start()
#     p.join()#那么我们可以用到 join 方法，join 方法的主要作用是：阻塞当前进程，直到调用 join 方法的那个进程执行完，再继续执行当前进程。


class Clockp2(multiprocessing.Process):
    def __init__(self,name,interval):
        multiprocessing.Process.__init__(self)
        self.interval=interval
        self.name=name

    def run(self):
        print('进程的序号{0}进程pid{1}'.format(self.name,os.getpid()))
        start=time.time()
        time.sleep(random.random()*3)
        end=time.time()
        print('进程{0}运行了{1}秒'.format(self.name,start-end))




# if __name__=='__main__':
#     print('主进程的pid{0}'.format(os.getpid()))
#     p=Pool(3)
#     for i in range(9):
#         p.apply_async(run,args=(i,))
#     p.close()# Pool 对象调用 join() 方法会等待所有子进程执行完毕，调用 join() 之前必须先调用 close() ，调用close() 之后就不能继续添加新的 Process 了。
#     p.join()
#






