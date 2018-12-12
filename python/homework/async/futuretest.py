import asyncio
import time
from functools import partial
# 偏函数  专门用来解决 当以函数名作为传入参数，但无法再传入传入函数的参数的问题。比如下面的add_done_callback


async def get_html(url):
    print('start get url')
    await asyncio.sleep(2)     # 必须加await实现协程   这里asyncio.sleep(2)是一个子协程，time.sleep不能可await搭配.
    # time.sleep(2)  # 不会报错， 但在协程里不要使用同步的io操作
    print('end get url')
    return 'cannon'


# 回调函数必须有个future传入参数，否则会报错。 这与add_done_callback函数有关
def callback(url, future):  # 回调函数， 如果有传入参数， 必须放在future前面。这点比较特殊
    print(url)


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()         # 开始时间循环
    get_future = asyncio.ensure_future(get_html('http://baidu.com')) # 类似多线程得到的future
    # 或者get_future = loop.create_task(get_html('http://baidu.com'))

    # get_future.add_done_callback(callback)   # 执行完以后执行callback
    get_future.add_done_callback(partial(callback, 'www.baidu.com'))   # callback如果要传入参数， 使用partial实现
    loop.run_until_complete(get_future)
    print(get_future.result())    # future的result方法得到返回值， 类似多线程ThreadPoolExecutor