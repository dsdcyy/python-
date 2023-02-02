import time
from multiprocessing import Process, Pipe


# 通过pipe实现进程间通信
# from multiprocessing import Queue
# from queue import Queue
# from multiprocessing.Manager import Queue
def producer(pipe):
    pipe.send('bodylist')
    time.sleep(1)


def consumer(pipe):
    time.sleep(1)

    print(pipe.recv())


if __name__ == '__main__':
    # Pipe只能适用于两个进程,但性能优于Queue
    recv, send = Pipe()
    my_producer = Process(target=producer, args=(send,))
    my_consumer = Process(target=consumer, args=(recv,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()
