# eval 执行输入的字符串表达式

res = eval(input('>>>'))
# __import__('os').system('ls') 可以导入模块并执行系统命令，需要慎用
print(res, type(res))

# exec 执行代码块
# vars == __dict__
print(vars(type(res)))