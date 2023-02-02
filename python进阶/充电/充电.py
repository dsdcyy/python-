from time import sleep
def alfred(num):
    for i in range(num,101):
        sleep(0.05)
        print(f'\r当前电量:{"|"*i} {i}%',end='')
        
if __name__ == '__main__':
    alfred(0)