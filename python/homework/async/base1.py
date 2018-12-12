# import asyncio,time
#
# @asyncio.coroutine
# def get1():
#     print('start get')
#     yield from asyncio.sleep(2)
#     print('end get')
#
#
#
# loop=asyncio.get_event_loop()
# loop.run_until_complete(get1())


# import asyncio, time
#
#
#
# async def get1(i):
#     print('start get',i)
#     await asyncio.sleep(2)
#     print('end get',i)
#
#
#
# loop = asyncio.get_event_loop()
# task=list()
# for i in range(9):
#     task.append(get1(i))
#
# loop.run_until_complete(asyncio.wait(task))


import asyncio,time

async def get2():
    print('sta')
    result=await get1()
    print('en')
    return result

async def get1():
    print('start get')
    await asyncio.sleep(2)
    print('end get')
    return 'gggget'



loop=asyncio.get_event_loop()
result=loop.run_until_complete(get2())
print(result)