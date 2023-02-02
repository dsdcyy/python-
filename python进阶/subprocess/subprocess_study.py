import subprocess

# 执行系统命令
# 命令 在系统终端执行 stdout 执行结果 subprocess.PIPE 管道  stderr 执行错误结果
obj = subprocess.Popen('ls &&  1',
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
# 获取执行成功的信息
res = obj.stdout.read()
# decode 进行编码解码 使用系统的字符集即可
print(res.decode('utf-8'))
# 获取执行失败的信息
error_res = obj.stderr.read()
print(error_res.decode('utf-8'))
