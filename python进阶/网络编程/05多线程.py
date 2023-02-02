import threading
import time
from time import sleep


def func():
    print('func:starting')
    sleep(1)
    print('func:waiting for')
    sleep(1)
    print('func:ending')


def func2():
    print('func2:starting')
    sleep(1)
    print('func2:waiting for')
    sleep(1)
    print('func2:ending')


# 继承自类
class Thread_Class(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(f'{self.name}:starting')
        sleep(1)
        print(f'{self.name}:waiting for')
        sleep(1)
        print(f'{self.name}:ending')


# 继承自类
if __name__ == '__main__':
    # th1 = Thread(target=func)
    # th2 = Thread(target=func2)
    # # 设置守护进行，随着主线程的关闭而关闭 th1.daemon
    # # th1.daemon = True
    # # th2.daemon = True
    #
    # t1 = time.time()
    # th1.start()
    # th2.start()
    # # join 堵塞，只有运行完本线程才能运行其它线程,th1和th2是并列的
    # th1.join()
    # th2.join()
    # t2 = time.time()
    # # 由于线程是并列的，所以打印并不会等th1,th2结束，它运行在主线程
    # print('Total time: %.4f seconds' % (t2 - t1))
    th1 = Thread_Class('func')
    th2 = Thread_Class('func2')
    t1 = time.time()
    th1.start()
    th2.start()
    # join 堵塞，只有运行完本线程才能运行其它线程,th1和th2是并列的
    th1.join()
    th2.join()
    t2 = time.time()
    # 由于线程是并列的，所以打印并不会等th1,th2结束，它运行在主线程
    print('Total time: %.4f seconds' % (t2 - t1))
