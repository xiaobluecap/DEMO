import asyncio
import time
from functools import partial


async def get_html(url):
    print('start get url', url)
    # 必须加await实现协程   这里asyncio.sleep(2)是一个子协程，time.sleep不能可await搭配.
    await asyncio.sleep(2)
    # time.sleep(2)  # 不会报错， 但在协程里不要使用同步的io操作
    print('end get url')
    return 'cannon'


def callback(url, future):
    print(url)


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()         # 开始时间循环

    tasks1 = [get_html('http://baidu.com') for i in range(3)]
    tasks2 = [get_html('http://google.com') for i in range(3)]
    group1 = asyncio.gather(*tasks1)    # gather可以进行分组
    group2 = asyncio.gather(*tasks2)
    loop.run_until_complete(asyncio.gather(group1, group2))
    print(time.time() - start_time)