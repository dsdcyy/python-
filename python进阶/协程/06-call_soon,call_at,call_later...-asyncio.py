import asyncio


def compute(x, y, loop):
    print(f"Compute {x}+{y}")
    print(loop.time())
    return x + y


def print_sum(x, y, loop):
    res = compute(x, y, loop)
    print(f'{x}+{y}={res}')


# 停止loop
def stop_loop(loop):
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    # call_soon 执行普通函数
    # loop.call_soon(print_sum, 3, 5)
    # loop.call_soon(stop_loop, loop)
    # call_later 在指定时间执行函数 ，更据等待时间的长短优先执行等待长的时间
    # loop.call_later(2, print_sum, 2, 5)
    # loop.call_later(3, print_sum, 3, 5)
    # loop.call_later(4, stop_loop, loop)
    # call_at 在内部时钟的时间上指定时间执行函数 ，更据等待时间的长短优先执行等待长的时间
    now = loop.time()
    loop.call_at(now + 2, print_sum, 2, 5, loop)
    loop.call_at(now + 3, print_sum, 3, 5, loop)
    loop.call_at(now + 4, stop_loop, loop)

    # 最后加上run_forever
    loop.run_forever()
