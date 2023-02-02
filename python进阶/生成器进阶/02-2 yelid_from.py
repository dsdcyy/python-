final_result = {}


# sales_sum 委托生成器 k 子生成器
def sales_sum(k):
    total = 0
    nums = []
    while True:
        x = yield
        print(k + '销量:', x)
        # 循环结束条件
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums


# middle 调用方
def middle(k):
    while True:
        final_result[k] = yield from sales_sum(k)
        print(k + '销量统计完成！')


def main():
    data_sets = {
        '面膜': [1200, 1500, 3000],
        '手机': [28, 55, 98, 108],
        '服装': [280, 560, 778, 70],
    }
    for k, v in data_sets.items():
        print('start key:', k)
        m = middle(k)
        next(m)
        for d in v:
            # send的值传入到了sales_sum中
            m.send(d)
        next(m)
    print('final_result', final_result)


if __name__ == '__main__':
    main()
