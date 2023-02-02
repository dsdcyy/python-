import sys

# sys.argv 获取从终端传入的参素
# 第一个元素是文件路径
x = sys.argv[0]
# 后面的元素为在终端输入的元素
y = sys.argv[1]
z = sys.argv[2]
print(x,y+z)