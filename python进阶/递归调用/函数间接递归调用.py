import time

def x1(num=0):
    print('x1',num)
    time.sleep(0.01)
    x2(num+1)
def x2(num=0):
    print('x2',num)
    x1(num+1)
if __name__ == '__main__':
    x1(0)
