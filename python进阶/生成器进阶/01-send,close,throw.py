def gen_func():
    # try:
    #     html = yield 'haha'
    #     print(html)
    # # 如果还有yelid，gen.close()会继续抛出异常
    # # RuntimeError: generator ignored GeneratorExit
    # except GeneratorExit:
    #     # raise StopIteration
    #     pass
    html = yield 'haha'
    print(html)
    yield 1

    return 'bounds'


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    # # close
    gen.close()
    # print(gen.send(10))
    # print(next(gen))
    print(('hello world'))
    # StopIteration :停止迭代，抛出返回值
    # throw 抛出异常
    gen.throw(Exception, 'Download Error!')
