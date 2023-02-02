class Person(object):
    obj = None

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if not cls.obj:
            cls.obj = super().__new__(cls)
        return cls.obj


p1 = Person('张三', 20)
p2 = Person('张三', 85)
print(p1, p2)
