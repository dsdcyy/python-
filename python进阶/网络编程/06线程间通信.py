import threading
import time
from time import sleep
from threading import Thread

# 共享变量
url_set = set()


# 继承自类
def func(url_set:set):
    print('func:starting')
    sleep(0.5)
    while True:
        if len(url_set):
            url = url_set.pop()
            print('func:waiting for')
            sleep(0.5)
            print(url)
            print('func:ending')
        else:
            break


def func2(url_set:set):
    print('func2:starting')
    sleep(0.5)
    print('func2:waiting for')
    for i in range(1, 21):
        url_set.add(f'https://www.google.com/{i}')
    sleep(0.5)
    print('func2:ending')


if __name__ == '__main__':
    th1 = Thread(target=func2, args=(url_set,))
    th1.start()
    th1.join()
    for i in range(len(url_set)):
        th2 = Thread(target=func, args=(url_set,))
        th2.start()
