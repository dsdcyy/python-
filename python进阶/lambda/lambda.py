# lambda 隐匿函数
# 用于一行代码实现一个功能，且使用完后会被销毁
print((lambda x,y : x+y)(1,2))

info = {
    'jack':5000,
    'tony':7000,
    'andy':8000,
    'amy':6000,
    'lucy':11000
}
# key参数 比价依据
print(max(info,key=lambda k:info[k]))

l = ['康师傅',"统一",'大今野','白象']
# map使用.函数,可迭代对象
l1 = map(lambda x:x+'老坛酸菜',l)
print(l1.__next__())