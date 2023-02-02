import random
from functools import wraps
import time
def outer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time   = time.time()
        print('执行时间：{:.4f}s'.format(end_time-start_time))

        return result
    return wrapper
l = sorted([random.randint(1,1000000) for i in range(1000000)])
def 二分法(l,s=187658):

    half = len(l) / 2 if len(l) % 2 == 0 else len(l)/2+0.5

    half = int(half)

    if s > l[half]:
        l = l[half:]
    elif s == l[half]:
        print("找到了！")
        return
    else:
        l = l[:half]
    # print(l)
    if len(l)>1:
        二分法(l)
    else:
        print("数字未找到")
@outer        
def main():
    二分法(l)
if __name__=='__main__':
    main()