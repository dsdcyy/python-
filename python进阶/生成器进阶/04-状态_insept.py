import inspect


# 生成值处理值，可以看作协程
def gun_func():
    value = yield 1
    return 'boddy'


# 用同步的方法编写异步的代码

if __name__ == '__main__':
    gen = gun_func()
    # 查看生成器状态
    # 为调用next方法状态 GEN_CREATED
    print(inspect.getgeneratorstate(gen))
    next(gen)
    # 调用过的状态 GEN_SUSPENDED 暂停
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration:
        pass
    # 取完数据后的状态 GEN_CLOSED 关闭
    print(inspect.getgeneratorstate(gen))
