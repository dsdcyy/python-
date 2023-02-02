import asyncio


async def compute(x, y):
    print(f"Compute {x}+{y}")
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    res = await compute(x, y)
    print(f'{x}+{y}={res}')


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    task = loop.create_task(print_sum(4, 5))
    loop.run_until_complete(asyncio.gather(task))
