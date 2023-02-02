# coding: utf-8
# @Author: 小飞有点东西
import random
from 二分法 import outer

def binary_search(l, target):
    """
    二分法算法
    :param l:  # 要切片的列表
    :param target:  # 要查找的值
    :return: # 不存在查找的值，就结束递归
    """

    # print(l)
    if len(l) == 0:  # 当最后切出来的列表为空的时候，就说明值不存在
        print('该值不存在')
        return

    mid_index = len(l) // 2  # 获取列表中间的索引，
    # //是取整除，返回商的部分。如果len的值是偶数，那它拿到的就是中间靠右的值（主要是为了切掉一半，所以切左边一个和切右边一个，关系都不大）

    mid_value = l[mid_index]  # 获取列表中间的值

    if target > mid_value:  # 如果要找的值大于列表中间的值
        l = l[mid_index + 1:]  # 用切片拿到列表的右半部分（注意顾前不顾后，mid_index已经比较过了，所以切片的时候切掉它）
        binary_search(l, target)  # 把切好的新列表，传入下一次递归
    elif target < mid_value:  # 如果要找的值小于列表中间的值
        l = l[:mid_index]  # 用切片拿到列表的左半部分（同样顾前不顾后，mid_index不会被切到新列表里面）
        binary_search(l, target)  # 把切好的新列表，传入下一次递归
    else:
        print('找到了')  # 不大于也不小于，就等于找到了
@outer
def main():
    binary_search(l, 187658)

if __name__ == '__main__':
    l = sorted([random.randint(1,1000000) for i in range(1000000)])
    main()
