# 多进程编程
# 耗cpu的操作，io操作 使用多线程

from 装饰器.无参装饰器 import outer
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# import functools


# @functools.lru_cache
def fblq(n: int) -> int:
    if n < 2:
        return n
    # n-1的值
    n1 = 1
    # n-2的值
    n2 = 0
    # 结果值
    res = 0
    # 从2到n循环
    for i in range(2, n + 1):
        # 获得此时的结果
        res = n1 + n2
        # 将n-1的结果赋给n-2
        n2 = n1
        # 将结果值赋给n-1
        n1 = res
    return res


def fbnq3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


@outer
def main():
    res = [fblq(n) for n in range(300)]
    print('未使用多线程多进程：', res)


@outer
def main2():
    with ThreadPoolExecutor(3) as t:
        res = [i for i in t.map(fblq, range(300))]
        print('使用线程池:', res)


@outer
def main3():
    with ProcessPoolExecutor(3) as p:
        res = [i for i in p.map(fblq, range(300))]
        print('使用进程池:', res)


if __name__ == '__main__':
    main()
    main2()
    main3()
