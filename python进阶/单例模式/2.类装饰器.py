from functools import wraps


def Singleton_mode(cls):
    obj = None
    @wraps(cls)
    def wrapper(*args, **kwargs):
        nonlocal obj
        if not obj:
            obj = cls(*args, **kwargs)
        return obj

    return wrapper


@Singleton_mode
class Person(object):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

p1 = Person('张三', 20)
p2 = Person('张三', 85)

print(p1, p2)