import pickle
from 序列化 import dic

# 序列化

# 解决乱码
# res = pickle.dumps(dic,protocol=0)

# print(res,type(res))

# 写入到文件
# 方法1 pickle.dumps()
# with open('序列化和反序列化/data.pickle','wb') as f:
#     f.write(res)
# 方法2 pickle.dumps()
# with open('序列化和反序列化/data2.pickle','wb') as f:
#     pickle.dump(dic,f,0)

# 反序列化

# # 方法1 pickle.loads() 将二进制字符串转换为字典格式数据
# with open('序列化和反序列化/data.pickle','rb') as f:
#     res_pickle = f.read()
# print(pickle.loads(res_pickle))

# 方法1 pickle.loads() 将二进制字符串转换为字典格式数据
with open('序列化和反序列化/data2.pickle','rb') as f:
    res_pickle = pickle.load(f)
print(res_pickle)