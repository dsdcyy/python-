from queue import Queue
from time import sleep
from threading import Thread


# 共享变量

# 继承自类
def func(queue:Queue):
    print('func:starting')
    sleep(0.5)
    # 堵塞方法，如果队列为空，则一致堵塞着
    url = queue.get()
    print('func:waiting for')
    sleep(0.5)
    print(url)
    print('func:ending')


def func2(queue:Queue):
    print('func2:starting')
    sleep(0.5)
    print('func2:waiting for')
    for i in range(1, 21):
        queue.put(f'https://www.google.com/{i}')
    sleep(0.5)
    print('func2:ending')


if __name__ == '__main__':
    url_queue = Queue(maxsize=1000)
    # 判断队列是否为空
    # url_queue.empty()
    # 判断队列长度
    # url_queue.qsize()
    th1 = Thread(target=func2, args=(url_queue,))
    th1.start()
    # 如果url_queue没有获取到数据则会阻塞在这
    # url_queue.join()
    # 结束程序
    # url_queue.task_done()
    for i in range(20):
        th2 = Thread(target=func, args=(url_queue,))
        th2.start()
