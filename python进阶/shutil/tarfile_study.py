import tarfile

# 压缩
tar = tarfile.open('11.tar','w') # 创建压缩文件
tar.add('3.txt') # 添加需要压缩的文件
tar.add('4.txt')
tar.close() # 关闭压缩文件

# 解压
tar = tarfile.open('11.tar','r') # 打开一个压缩文件
tar.extractall(path='txt') # 解压缩所有文件并指定解压路径
tar.close() # 关闭压缩文件