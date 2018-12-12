import asyncio


async def one():
    print('in one')
    return 'one'


async def two(arg):
    print('in two')
    return 'two with arg {}'.format(arg)


async def outer():
    print('in outer')
    print('waiting for one')
    result1 = await one()
    print('waiting for two')
    result2 = await two(result1)
    return result1, result2


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(outer())
    print('result value: {!r}'.format(return_value))
finally:
    event_loop.close()