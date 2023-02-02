import zipfile
# 压缩
# zf = zipfile.ZipFile('10.zip','w')
# # 需要加到压缩包的文件
# zf.write('7.txt')
# zf.write('8.txt')
# # 关闭压缩包
# zf.close()

# 解压
zf = zipfile.ZipFile('10.zip','r') # 打开一个压缩包
zf.extractall(path='txt') # 解压缩全部文件,且指定解压路径
zf.close()
