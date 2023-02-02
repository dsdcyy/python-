# 元类
class Mytype(type):
    obj = None

    def __call__(self, *args, **kwds):
        if not self.obj:
            # self.obj = super().__call__(*args, **kwds)
            self.obj = self.__new__(self)
        self.__init__(self.obj, *args, **kwds)
        return self.obj


class Singleton_Mode(metaclass=Mytype):
    ...


# metaclass 将元类改为自己定义的类
class Person(Singleton_Mode):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


p1 = Person('张三', 20)
print(p1, p1.__dict__)
p2 = Person('张三', 85)
print(p2, p2.__dict__)
