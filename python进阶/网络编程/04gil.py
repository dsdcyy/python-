# global interpreter lock
# python中的一个线程对应于c语言的一个线程
# gil使得同一时刻只有一个线程在cpu上执行字节码，无法将多个线程映射到多个cpu上执行
# gil会根据执行的字节码函数以及时间线进行释放，或者遇到io的操作时主动释放
import dis
from threading import Thread
from 装饰器.无参装饰器 import outer


def add(x, y):
    return x + y


# print(dis.dis(add))


def add_sum(num):
    return num


@outer
def main(s):
    for i in range(s):
        add_sum(i)


@outer
def main2(s):
    for i in range(s):
        th1 = Thread(target=add_sum, args=(i,))
        th1.start()


if __name__ == '__main__':
    pass
