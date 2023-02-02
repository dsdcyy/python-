l = [1, 2, [3, [4, [5, [6, [7, [8, [9, [10, [11, 12]]]]]]]]]]


# l  = [1,2,[3,4]]

def func(li):
    for i in li:
        if type(i) is list:
            func(i)
        else:
            print(i)


func(l)
