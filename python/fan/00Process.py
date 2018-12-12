# from multiprocessing import Process
# import os,time
#
# def run():
#     print('进程开始')
#     time.sleep(3)
#     print('进程结束')
#
#
# if __name__=='__main__':
#     a=Process(target=run)
#     a.start()
#     a.join()

# from multiprocessing import Process,Pool
# import time,random
#
#
# def Run(i):
#     print('子进程开始----%d'%(i))
#     a=random.choice([1,4,3])
#     time.sleep(a)
#     print('子进程结束',a)
#
#
# if __name__=='__main__':
#     print('父进程开始')
#     pp=Pool(4)
#
#     for i in range(10):
#         pp.apply_async(Run,args=(i,))
#     pp.close()
#     pp.join()
#     print('‘父进程结束')














