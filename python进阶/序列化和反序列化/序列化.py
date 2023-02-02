# 序列化：把内存中的数据类型转成一种特定的格式，这种格式可以用来存储或者传输给其它平台 
# 内存中的数据类型 --->序列化 ---> 特定格式(json/pickle)

# 用途:
# 1.存档
# 2.跨平台数据交互

# 序列化
import json

dic = {
    'name': '张三',
    'age': 18,
    '爱好': ['吃饭', '睡觉', '打豆豆', '打游戏'],
    '体重': 60.5,
    'married': False,
    # 'set':{1,2,3,4}
}
# json.dumps() 将字典数据转换为json字符串
json_res = json.dumps(dic, ensure_ascii=False)

# 将数据保存到磁盘

# 方法1
# with open('序列化和反序列化/data.json','wt',encoding='utf-8') as f:
#     f.write(json_res)

# 方法2
# with open('序列化和反序列化/data2.json','wt',encoding='utf-8') as f:
#     # 直接进行转换并写入文件
#     json.dump(dic,f,ensure_ascii=False)
