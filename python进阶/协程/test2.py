from 装饰器.无参装饰器 import outer


# 速度较快，但代码量较大
@outer
def test(num):
    x_list = []
    for i in range(1, num + 1):
        j = str(i)
        if i < 10:
            x_list.append('000' + j)
        elif i < 100:
            x_list.append('00' + j)
        elif i < 1000:
            x_list.append('0' + j)
        else:
            x_list.append(j)
    return x_list


# 改良,执行最慢
@outer
def test2(num):
    x_list = []
    for i in range(1, num + 1):
        x_list.append('0' * (4 - len(str(i))) + str(i))
    return x_list


# 代码简洁，比2快点
@outer
def test3(num):
    x_list = ['0' * (4 - len(str(i))) + str(i) for i in range(1, num + 1)]
    return x_list


# 比3快点，代码比1少，速度第2,速度损失极少
@outer
def test4(num):
    x_list = []
    dic = {1: '000', 2: '00', 3: '0', 4: '', 5: '', 6: '', 7: '', 8: ''}
    for i in range(1, num + 1):
        j = str(i)
        x_list.append(dic[len(j)] + j)
    return x_list


if __name__ == '__main__':
    print(test(1000000)[-10:])
    print(test2(1000000)[-10:])
    print(test3(1000000)[-10:])
    print(test4(1000000)[-10:])
    """
        执行时间：0.1247s
        ['999991', '999992', '999993', '999994', '999995', '999996', '999997', '999998', '999999', '1000000']
        执行时间：0.1899s
        ['999991', '999992', '999993', '999994', '999995', '999996', '999997', '999998', '999999', '1000000']
        执行时间：0.1721s
        ['999991', '999992', '999993', '999994', '999995', '999996', '999997', '999998', '999999', '1000000']
        执行时间：0.1250s
        ['999991', '999992', '999993', '999994', '999995', '999996', '999997', '999998', '999999', '1000000']
    """
