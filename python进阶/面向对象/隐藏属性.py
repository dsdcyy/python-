# 隐藏属性作用：隔离复杂度

class Test(object):
    def __init__(self, name:str, age:int):
        self.__name = name
        self.__age = age
    # 隐藏 在名前面加上__
    def __func1(self):
        print('我是隐藏方法func1')
    def get_name(self):
        return self.__name
    @property # 获取age属性 
    def age(self):
        return self.__age
    @age.setter # 修改age属性
    def age(self,new_age:int):
        if type(new_age) is not int:
            print('传入值不符合整型要求')
            return
        if not 0<=new_age<=150:
            print('年龄是否不符合常理认知？')
            return
        self.__age = new_age
        return self.__age
    def set_name(self,new_name:str):
        if type(new_name) is not str:
            print('传入值不符合整型要求!')
            return
        self.__age = new_name
        return self.__age
    @age.deleter # 删除age属性
    def age(self):
        del self.__age
    # property 将调用方法伪装成访问属性
    # 将age的三个方法伪装为self.age  self.age = xxx del self.__age
    # 顺序必须为查改删
    # age = property(get_age,set_age,del_age)
p1 = Test('张三',18)

print(p1.get_name(),p1.age)

p1.age = 201
print(p1.age)