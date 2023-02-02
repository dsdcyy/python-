import hashlib
import os
import json


def get_hash(dir_path: str):
    hash_json = []
    for file in os.listdir(dir_path):
        file = os.path.join(dir_path, file)
        m1 = hashlib.md5()
        with open(file, 'rb') as f:
            # m1 = hashlib.md5(f.read())
            # 让指针移动到文件末尾
            f.seek(0, 2)
            # 获取指针的位置,此时在末尾记得到文件大小
            size = f.tell()
            # print(size)
            # 获取1/10
            one_tenth = size // 10

            for i in range(10):
                # 指针移到文件开头，并参照开头
                f.seek(i * one_tenth, 0)
                # 读取多少个字节
                res = f.read(100)
                m1.update(res)
            hash_json.append({file: m1.hexdigest()})
    with open(dir_path.rsplit('/', 1)[1] + '.json', 'w', encoding='utf-8') as f:
        json.dump(hash_json, f, ensure_ascii=False)


def rm_sample_hash(hash_json1, hash_json2):
    with open(hash_json1, 'r') as f1, open(hash_json2, 'r') as f2:
        print('String')
        res_json1 = json.load(f1)
        res_json2 = json.load(f2)
        hash_value1 = [[i.get(j) for j in i][0] for i in res_json1]
        hash_value2 = [[i.get(j) for j in i][0] for i in res_json2]
        sample_hash = set(hash_value1) & set(hash_value2)
        print(sample_hash)
        # for i in hash_value2:
        #     try:
        #         if hash_value1[i]:
        #             print(hash_value1[i])
        #     except:
        #         print('没有')
        #         continue


if __name__ == '__main__':
    # get_hash('/media/Ljw/Data/xchina/fl/摄影师心已抖（抖叔） 摄影师心已抖（抖叔）作品：2021.11 - 2022.01')
    rm_sample_hash('摄影师心已抖（抖叔） 摄影师心已抖（抖叔）作品：2021.11 - 2022.01.json', '摄影师心已抖（抖叔） 摄影师心已抖（抖叔）作品集.json')
    ...
