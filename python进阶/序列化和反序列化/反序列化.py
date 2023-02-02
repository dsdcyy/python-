# 内存中的数据类型 <--- 反序列化 <--- 特定格式(jaon/pickle)
import json
# print(json.__name__)
import ujson


# print(json.__name__)

# 猴子补丁
def monkey_patch_json():
    json.__name__ = 'ujson'
    json.dumps = ujson.dumps
    json.loads = ujson.loads
    json.dump = ujson.dump
    json.load = ujson.load


monkey_patch_json()
if __name__ == '__main__':
    # 反序列化

    # 方法1
    # 从文件读取json字符串
    # with open('序列化和反序列化/data.json', 'rt') as f:
    #      res_json = f.read()
    # # loads()json字符串转换为字典类型数据
    # print(json.loads(res_json))

    # 方法2
    with open('序列化和反序列化/data.json', 'rt') as f:
        res_json = json.load(f)
    print(res_json)
