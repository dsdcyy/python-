import time
from multiprocessing import Process, Queue, Manager, Pool


def producer(queue: Queue):
    queue.put('a')
    time.sleep(1)


def consumer(queue: Queue):
    time.sleep(1)
    data = queue.get()
    print(data)


if __name__ == '__main__':
    # queue = Queue(10)
    # my_producer = Process(target=producer, args=(queue,))
    # my_consumer = Process(target=consumer, args=(queue,))
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()
    # 共享全局变量不适用于多进程编程
    # multiprocessing的queue无法直接用于pool池
    # 使用Manager().Queue
    queue = Manager().Queue(10)
    pool = Pool(2)
    pool.apply_async(producer, args=(queue,))
    pool.apply_async(consumer, args=(queue,))
    pool.close()
    pool.join()
