# hash(哈希)
# md5
# sha1
# sha256
# sha512

# hash值
# 1 输入敏感
# 2 不可逆
# 3 计算极快而长度固定

# 用途
# 1 密码加密
# 2 文件完整校验
import hashlib
# # md5加密
# h1 = hashlib.md5()
# h1.update(b'ljw')
# h1.update(b'123')
# # 相当于md5加密了'ljw123
# print(h1.hexdigest())
# # 其他加密一样，该加密方法即可

# h1 = hashlib.sha512()
# h1.update(b'ljw')
# h1.update(b'123')
# # 相当于md5加密了'ljw123
# print(h1.hexdigest())

# # 校验文件完整性
# # 1.校验整个文件
# with open('/home/Ljw/Downloads/Python-3.11.0.tar.xz','rb') as f:
#     m1 = hashlib.md5(f.read())
#     print(m1.hexdigest())
# 2.取文件的几个点进行计算
# path = '/home/Ljw/Downloads/Python-3.11.0.tar.xz'
# m1 = hashlib.md5()
# with open(path,'rb') as f:
#     # 让指针移动到文件末尾
#     f.seek(0,2)
#     # 获取指针的位置,此时在末尾记得到文件大小
#     size = f.tell()
#     # print(size)
#     # 获取1/10
#     one_tenth = size // 10
    
#     for i in range(10):
#         # 指针移到文件开头，并参照开头
#         f.seek(i*one_tenth,0)
#         # 读取多少个字节
#         res = f.read(100)
#         m1.update(res)
#     print(m1.hexdigest())

# 密码加盐

h2= hashlib.md5()
passwd = 'wxwx12345'
yan =  '天青色等烟雨,而我在等你'
h2.update((passwd[:2]+yan[2:4]).encode('utf-8'))
h2.update((passwd[2:4]+yan[4:]).encode('utf-8'))
h2.update((passwd[4:]+yan[:2]).encode('utf-8'))
res = h2.hexdigest()
print(res)