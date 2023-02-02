from lib.logger import logger

def login():
    print('执行登入功能'.center(30,'*'))
    logger('用户登入了！')
    
def register():
    print('执行注册功能'.center(30,'*'))
    logger('有用户注册了！')
    
def recharge():
    print('执行充值功能'.center(30,'*'))
    logger('用户充值了！')
    
def transfer():
    print('执行转账功能'.center(30,'*'))
    logger('用户转账了！')
    
func_dict = {
    '1': ('登入',login),
    '2': ('注册',register),
    '3': ('充值',recharge,),
    '4': ('转账',transfer,),
    '0': ('退出',exit),
}

def main():
    logger('用户使用了程序')
    while True:
        for key in func_dict:
            print(key,func_dict[key][0])
        opt = input('请选择功能：').strip()
        if opt not in func_dict:
            print('\033[33m不存在该功能\033[0m')
            continue
        func_dict[opt][1]()
    