# 时间循环+回调(驱动生成器)+epoll(IO多路复用)
# asyncio是python用于解决异步io编程的一整套解决方案
# tornado,gevent,twisted(scrapy,django channels)
# tornado(实现web服务器),django+flask
# tornado可以直接部署,nginx+tornado
from 装饰器.无参装饰器 import outer
import asyncio
from functools import partial


async def get_html(url):
    print('start get url')
    # 耗时操作需要等待
    await asyncio.sleep(2)
    print('end get url')
    return 'bobby'


def callback(url, future):
    print(url)
    print('send email to bobby!')


@outer
def main():
    # 事件循环
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_html('http://localhost:8080'))
    #  asyncio.ensure_future 获取future对象
    # get_future = asyncio.ensure_future(get_html('http://localhost:8080'))
    # task = [get_html('http://localhost:8080/') for i in range(10)]
    # asyncio.run(asyncio.wait(task))
    # 运行future对象 run_until_complete
    # loop.run_until_complete(get_future)
    # 获取函数返回值
    # print(get_future.result())
    # loop.create_task
    # task = loop.create_task(get_html('http://localhost:8080'))
    # add_done_callback task任务执行完后执行的函数
    # partial 将一个函数包装为另一个函数，返回的是函数名称,可以解决函数传参问题
    # task.add_done_callback(partial(callback, 'http://localhost:8080'))
    # loop.run_until_complete(task)
    # print((task.result()))
    # task = [get_html('http://localhost:8080') for i in range(10)]
    # asyncio.run(asyncio.gather(*task))
    # loop.run_until_complete(asyncio.gather(*task))
    # gather 和 wait 的区别
    """
        gather更加高级，除了可以完成wait的功能外还能对tasks分组
        取消任务 cancel
    """
    grp1 = [get_html('http://localhost:8080') for i in range(2)]
    grp2 = [get_html('http://localhost:8080') for i in range(4)]
    # grp1 = asyncio.gather(*grp1)
    # 取消任务
    # grp1.cancel()
    # grp2 = asyncio.gather(*grp2)
    # 同时处理两组数据
    loop.run_until_complete(asyncio.gather(*grp1, *grp2))
    # loop.run_until_complete(asyncio.gather(grp1, grp2))


if __name__ == '__main__':
    main()
