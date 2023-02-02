import time
from functools import wraps


def g_outer(name: str):
    def outer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(name)
            t1 = time.time()
            time.sleep(1)
            result = func(*args, **kwargs)
            t2 = time.time()
            print('程序运行时间:{:.4f}s'.format(t2 - t1))
            return result

        return wrapper

    return outer


@g_outer('helllo world！')
def test_print():
    print('hello world')


if __name__ == '__main__':
    test_print()
