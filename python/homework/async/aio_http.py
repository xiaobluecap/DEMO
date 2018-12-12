
#官网 https://aiohttp.readthedocs.io/en/stable/
import aiohttp
import asyncio

num = 0

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        global num
        num += 1
        print('------------{}'.format(num))
        # print(html)

#asyncio 高并发库
def tasks():
    task = list()
    for i in range(114499,114999):
        # 114499 http://blog.jobbole.com/114499/
        task.append(main("http://blog.jobbole.com/{}/".format(i)))
    return task



loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks()))