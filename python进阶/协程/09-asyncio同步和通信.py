import asyncio
from asyncio import Lock, coroutine

import aiohttp

cache = {}
lock = Lock()


# @coroutine
async def get_stuff(url):
    # await with lock:
    # 需要的代码段使用锁
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET', url)
        cache[url] = stuff
        return stuff


async def parse_stuff():
    stuff = await get_stuff('https://www.baidu.com')


async def use_stuff():
    stuff = await get_stuff('http://www.baidu.com')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [parse_stuff(), use_stuff()]
    loop.run_until_complete(asyncio.wait(tasks))
