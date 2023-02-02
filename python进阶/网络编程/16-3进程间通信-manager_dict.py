from multiprocessing import Process, Manager


def add_manager_dict(__manager_dict, key, value):
    __manager_dict[key] = value


if __name__ == '__main__':
    # 两个进程一起操作这个字典
    manager_dict = Manager().dict()
    add_manager_dict_1 = Process(target=add_manager_dict, args=(manager_dict, '22', 30,))
    add_manager_dict_2 = Process(target=add_manager_dict, args=(manager_dict, '25', 50,))
    add_manager_dict_1.start()
    add_manager_dict_2.start()
    add_manager_dict_1.join()
    add_manager_dict_2.join()
    print(manager_dict)
