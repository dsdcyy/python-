from 装饰器.无参装饰器 import outer
import sys
sys.setrecursionlimit(1000)


def my_sum(i):
    if i == 0:
        return 0
    # 递推：每次向后相加都需要问到自己
    # 回归：从自己开始算返回值
    return i + my_sum(i - 1)


@outer
def main():
    print(my_sum(100))


if __name__ == '__main__':
    main()
