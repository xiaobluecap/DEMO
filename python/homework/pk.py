from concurrent.futures import ThreadPoolExecutor,as_completed
import time,random
from functools import partial

# def consume(num):
#     time.sleep(num)
#     print('consume',num)
#
# pools=ThreadPoolExecutor(7)
#
# num =1
# while True:
#     time.sleep(0.6)
#     s=pools.submit(consume,(num))
#     pools.submit(consume,1)
#     pools.submit(consume,1)
#     pools.submit(consume,1)
#     pools.submit(consume,1)
#     pools.submit(consume,1)
#     pools.submit(consume,1)
#
#     print(s.done())
#
#     num+=1

def get_html(sleep_time,num):
    time.sleep(sleep_time)
    print('get page{}success'.format(sleep_time))
    return sleep_time,num



excutor =ThreadPoolExecutor(5)

#
# task1=excutor.submit(get_html,1)
# task2=excutor.submit(get_html,1)
# task3=excutor.submit(get_html,1)
#
# print(task3.cancel())
#
# print(task1.done())
#
# print(task1.result())
#
# print(task2.result())
# print(task1.done())



tasks=list()

for i in range(9):
    sleep_time=random.randint(2,8)
    tasks.append(excutor.submit(partial(get_html,sleep_time),(i)))

for i in as_completed(tasks):
    data =i.result()

    print('num{}'.format(data))
