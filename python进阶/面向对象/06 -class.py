# # class 干了些什么事情
# # 1.类名
# class_name = 'Human'
#
# # 2.基类
# base_class = (object,)
#
# # 3.执行类子代码，产生名称空间
# class_dict = {}
# class_sub_code = """
# def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# def info(self):
#     print('name:', self.name, 'age:', self.age)
#
# def __str__(self):
#     return f'<{self.name}:{self.age}>'
#
# def __del__(self):
#     print('delete:', self.name)
# """
# # 使用exec执行
# # 参数一：类子代码 参数二：类需要引用的全局名称空间的名字，参数三：类的名称空间
# exec(class_sub_code, {}, class_dict)
# print(class_dict)
#
# # 4.调用元类
#
# Human = type(class_name, base_class, class_dict)
# print(Human)
# obj = Human('张大山', 28)
# obj.info()


# 自定义元类

class MyType(type):
    # # Human = type(class_name, base_class, class_dict)
    # def __init__(self, class_name, base_class, class_dict):
    #     # 限制类名不能包含'_'
    #     if '_' in class_name:
    #         raise NameError('Class name contains "_". ')
    #     # 限制子类必须有文档注释
    #     if not class_dict.get('__doc__'):
    #         raise SyntaxError('Class must have a __doc__ attribute')
    #
    # # __new__ 在执行__init__之前执行 创建一个空对象
    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(cls, *args, **kwargs)
    # 在元类中重写__call__方法,当元类的对象进行实例化时会调用此方法,并返回生成好的对象
    def __call__(self, *args, **kwargs):
        self.obj = self.__new__(self)
        self.__init__(self.obj, *args, **kwargs)
        # 定制子类，在子类的属性前加上MyType_
        dic = {}
        for key in self.obj.__dict__:
            dic[f'MyType_{key}'] = self.obj.__dict__[key]
        self.obj.__dict__ = dic
        return self.obj


# 调用元类MyType的new方法产生一个空对象Human
# 调用元类MyType的init方法,初始化对象Human
# 返回初始化好的对象Human

class Human(metaclass=MyType):
    """ hello！"""

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def info(self):
    #     print('name:', self.name, 'age:', self.age)

    def __call__(cls, *args, **kwargs):
        print(f'{cls}.__call__!')

    def __str__(self):
        return f'{self.__class__.__name__}'


obj2 = Human('张大仙', 18)
# obj2.info()
# 对象()调用类call方法
obj2()
print(obj2.__dict__)
