# 元类：实例化产生类的类

# Human = 元类() class Human:pass
# 用class关键字定义的所有类都是由内置的元类type实例化产生的
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('name:', self.name, 'age:', self.age)

    # __str__ 打印对象时的结果
    def __str__(self):
        return f'<{self.name}:{self.age}>'

    def __del__(self):
        print('delete:', self.name)


obj = Human('张大仙', 73)
# Human的元类为type <class 'type'>
print(type(obj), type(Human), sep='\n')

print('*' * 50)
