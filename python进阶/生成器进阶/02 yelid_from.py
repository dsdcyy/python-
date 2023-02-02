from itertools import chain

my_list = [1, 2, 3, 4]
my_dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# chain 一次for循环将多个可迭代对象的值取出来
# for i in chain(my_list, my_dic, range(4)):
#     print(i)
# print(sum(range(100)))


def my_chain(*args, **kwargs):
    for i in args:
        # yelid from 将iterables对象的值直接取出来
        yield from i


# for i in my_chain(my_list, my_dic, range(4)):
#     print(i)
# print(sum(range(100)))

def func1(iterable):
    # 传入的是什么对象yiled返回的就是什么
    yield iterable


def func2(iterable):
    # yiled from 返回的是可迭代对象的值
    yield from iterable


# func3调用方 func2(委托生成器) iterable 子生成器

# yield from 会在调用方func3和子生成器iterable之间建立一个双向通道 yelid from 核心功能

def func3():
    g2 = func2()
    # 此时send的就是直接向func2的iterable发送值
    g2.send(None)


if __name__ == '__main__':
    for i in func1(range(10)):
        print(i)
    for i in func2(range(10)):
        print(i)
