from functools import wraps
import time


def outer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('执行时间：{:.4f}s'.format(end_time - start_time))

        return result

    return wrapper


@outer
def test_for(num):
    for i in range(num):
        print(i)


if __name__ == '__main__':
    test_for(10000)
