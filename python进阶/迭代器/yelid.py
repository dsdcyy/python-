def x(num: int):
    while True:
        print('here is %d' % num)
        # yelid表达式，可以传值并返回值
        y = yield num
        print(y, num)


if __name__ == '__main__':
    g = x(10)
    # next 继续执行被yelid暂停的函数
    print(next(g))
    # send 继续执行被yelid暂停的函数并且传值给yelid表达式

    g = x(20)
    print(g.send(None))
    print(g.send(20))
