class Test:
    def __init__(self):
        print('Hello world')


class Test2(Test):
    def __init__(self):
        super().__init__()

    pass


print(Test2.mro())

test = Test2()