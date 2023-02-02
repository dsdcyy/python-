# 形参:类型=默认值  -> 返回值类型

def func(name:str='张三',age:int=88) -> int:
    print(age)
    print(name)
    return age
if __name__ == '__main__':
    func()