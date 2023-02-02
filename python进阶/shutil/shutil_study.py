import shutil 

# 拷贝文件状态信息 如:atime,mtime,ctime 等4.txt必须存在
# shutil.copystat('3.txt','4.txt')

# 拷贝文件的权限 拷贝3.txt的权限给4.txt 4.txt必须存在
# shutil.copymode('3.txt','4.txt')

# 拷贝文件
# shutil.copyfileobj(open('3.txt','r'),open('5.txt','w')) # 打开老文件，写入新文件
# shutil.copyfile('3.txt','6.txt') # 拷贝文件
# shutil.copy('3.txt','7.txt') # 拷贝文件以及权限
# shutil.copy2('3.txt','8.txt') # 拷贝文件以及状态信息

# 拷贝文件夹
# 排除拷贝指定的文件 ignore shutil.ignore_patterns 使用正则表达式进行排除
# shutil.copytree('充电','充电2',ignore=shutil.ignore_patterns('*.py','user*'))

# 移动文件/文件夹 如果移动路径相同，则为重命名,类似Linux命令 mv
# shutil.move('5.txt','5_copy.txt')
# shutil.move('6.txt','txt/6.txt')

# 创建压缩文件('zip','tar','bztar','gztar')
# 压缩后的路径,压缩格式,被压缩的目录
shutil.make_archive('9','zip',root_dir='txt')