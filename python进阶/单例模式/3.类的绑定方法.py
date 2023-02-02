class Person(object):
    obj = None

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def get_obj(cls, *args, **kwargs):
        if not cls.obj:
            cls.obj = cls(*args, **kwargs)
        return cls.obj


p1 = Person.get_obj('张三', 20)
p2 = Person.get_obj('张三', 85)
print(p1, p2)
