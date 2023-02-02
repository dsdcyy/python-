import random
from 二分法 import outer
l = sorted([random.randint(1,1000000) for i in range(1000000)])
@outer
def for_test(l):
    for i in l:
        if i == 187658:
            print('找到了！')
if __name__ == '__main__':
    for_test(l) 