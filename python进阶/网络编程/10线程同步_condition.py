from threading import Thread, Condition
from 装饰器.无参装饰器 import outer


def add(cond: Condition):
    global total
    for i in range(1000):
        with cond:
            total += 1
            print('total+1:', total)
            # 通知desc函数
            cond.notify()
            # 等待desc消息
            cond.wait()


def desc(cond: Condition):
    global total
    for i in range(1000):
        with cond:
            # 等待add消息
            cond.wait()
            total -= 1
            print('total-1:', total)
            # 发送给add消息
            cond.notify()


@outer
def main():
    th1 = Thread(target=add, args=(condition,))
    th2 = Thread(target=desc, args=(condition,))
    # 执行时先等待的函数先执行
    # 调用with cond后才能调用notify方法
    th2.start()
    th1.start()
    th1.join()
    th2.join()
    print(total)


if __name__ == '__main__':
    total = 0
    # 获取condition对象
    condition = Condition()
    main()
