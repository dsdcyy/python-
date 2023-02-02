import time,datetime
# 1.时间戳 time.time()
# print(time.time())

# 2. 格式化的字符串格式:2022-11-16 12:06:30
# %Y-%m-%d 格式化 年-月-日
# %H:%M:%S 格式化 时:分:秒
# %A：输出英文星期几
# print(time.strftime('%Y-%m-%d %H:%M:%S %A'))
# %X 时:分:秒
# print(time.strftime('%Y-%m-%d %X %A'))
# %x 日/月/年
# print(time.strftime('%x %X %A'))

# 3.结构化时间 time.localtime()
# 里面的值均可用.取出来 如  time.localtime().tm_year 获得到的数据是整型的，可以直接用于计算
"""
time.struct_time(
        tm_year=2022, # 年份
        tm_mon=11, # 月份
        tm_mday=16, # 天
        tm_hour=12, # 小时
        tm_min=15, # 分钟
        tm_sec=29, # 秒
        tm_wday=2, # 一个星期的第几天,从星期天开始
        tm_yday=320, # 今天的第几天
        tm_isdst=0  # 是否是夏令时
)

"""
# print(time.localtime())

# 4.datetime
# replace microsecond 参数 等于0可以去掉微秒
# print(datetime.datetime.now().replace(microsecond=0))
# date.timedelta 计算时间

# 7天后
# print(datetime.datetime.now().replace(microsecond=0)+datetime.timedelta(days=7))

# 时间戳->结构化时间  time.localtime

# print(time.localtime(1111111111))

# 结构化时间->字符串格式时间 time.strftime
# res = time.localtime(1111111111)

# print(time.strftime('%Y-%m-%d %X %A',res))

# 字符串格式时间->结构化时间  time.strptime 

# t = '2012-08-22 20:05:56'

# print(time.strptime(t, '%Y-%m-%d %X'))

# 结构化时间转时间戳  time.mktime

# print(time.mktime(time.localtime()))

# 时间戳格式转字符串格式

print(datetime.datetime.fromtimestamp(time.time()))