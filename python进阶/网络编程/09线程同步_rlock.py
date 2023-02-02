from threading import RLock, Thread
from 装饰器.无参装饰器 import outer
# 适用于同一函数内
# RLock,可以多次调用lock.acquire(),但调用几次就得lock.release()几次
total = 0
lock = RLock()


def add():
    global total, lock
    for i in range(1000):
        # 获得锁
        lock.acquire()
        # 死锁
        # lock.acquire()
        total += 1
        print('total+1:', total)
        # 释放锁，如果不进行释放程序会停止
        lock.release()


def desc():
    global total, lock
    for i in range(1000):
        lock.acquire()
        lock.acquire()
        total -= 1
        print('total-1:', total)
        lock.release()
        lock.release()


@outer
def main():
    th1 = Thread(target=add)
    th2 = Thread(target=desc)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(total)


if __name__ == '__main__':
    main()
