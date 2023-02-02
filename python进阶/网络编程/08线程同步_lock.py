from threading import Lock, Thread
from 装饰器.无参装饰器 import outer

# lock 给要改变的变量加锁，只有我释放了锁其它线程才能修改
# 影响性能且容易死锁

# 死锁
# 函数a需要拿到a,b
# 函数b需要拿到a,b
# 1.当a函数拿到a时同时b函数拿到b,此时a会等待b释放b,b等待a释放a，形成死锁
# 2.lock.acquire()后继续lock.acquire()
total = 0
lock = Lock()


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
        total -= 1
        print('total-1:', total)
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
