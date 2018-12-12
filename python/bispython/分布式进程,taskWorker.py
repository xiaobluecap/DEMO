from multiprocessing.managers import BaseManager
import time
#创建类似的QueueManager
class QueueManager(BaseManager):
    pass
#第一步，使用QueueManager注册用于获取Queue的方法和名称
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
#第二步，链接到服务器
server_addr='127.0.0.1'
print('Connect to server %s'%server_addr)
#端口和验证口令保持与服务进程完全一致
m=QueueManager(address=(server_addr,9999),authkey='qiye')
#从网络连接
m.connect()
#获取queue的对象
task=m.get_task_queue()
result=m.get_result_queue()
#从task队列获取任务，并把结果写入result队列
while(not task.empty()):
    image_url=task.get(True,timeout=8)
    print('run task download %s'%image_url)
    time.sleep(1)
    result.put('---%s--->success'%image_url)

print('worker exit')