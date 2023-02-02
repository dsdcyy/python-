# 指定解释器路径,执行的时候可用不用加解释器
#!/home/Ljw/anaconda3/bin/python 
import sys

# 1. 内存
# 2. 磁盘  本文件，同级目录文件 lib/python*.zip lib/python*  lib/python* /lib-dynload lib/python3.10/site-packages
# 如果需要导入的路径不在,可以用path.append添加路径
sys.path.append(r'/media/Ljw/Data/Python/python进阶/装饰器')
print(sys.path)
from 无参装饰器 import outer

@outer
def main():
    print('hello')
    
if __name__ == '__main__':
    main()