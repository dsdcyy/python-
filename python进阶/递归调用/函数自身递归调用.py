import sys


def x(num=0):
    print(num)
    x(num + 1)


# 获取递归深度
# print(sys.getrecursionlimit())
# 修改递归深度
# sys.setrecursionlimit(1500)
# print(sys.getrecursionlimit())

# RecursionError: maximum recursion depth exceeded while calling a Python object
# 超出最大递归深度错误
if __name__ == "__main__":
    x(0)
