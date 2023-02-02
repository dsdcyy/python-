def my_chain(*args, **kwargs):
    for i in args:
        # yelid from 将iterables对象的值直接取出来
        yield from i


if __name__ == '__main__':
    res = my_chain(['a', 'b', 'c', 'd'], range(10))
    for i in res:
        print(i)
