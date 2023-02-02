# import os
# import time
#
# # 新建一个子进程，只能用于linux/unix中,子进程会在创建处重新运行一次此处后父进程的所有资源
# pid = os.fork()
# print('boot')
# if pid == 0:
#     print(f'子进程{os.getpid()},父进程是:{os.getppid()}')
# else:
#     print(f'我是父进程:{pid}')
# # 如果没有睡眠时间父进程会直接结束掉但字进程依然存在且无法退出
# time.sleep(2)
import multiprocessing


def get_html(n):
    # print('Processing susses...')
    return n


# class Get_html2(multiprocessing.process):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print(f'{self.name}:Processing susses...')


if __name__ == '__main__':
    # # 单个
    # process = multiprocessing.Process(target=get_html, args=(10,))
    # print(process.pid)
    # process.start()
    # print(process.pid)
    # process.join()
    # print('process finished')
    # # multiprocessing pool 进程池,默认使用cpu个数的进程数
    pool = multiprocessing.Pool()
    # # 异步提交任务
    # res = pool.apply_async(get_html, (10,))
    # # 调用join前必须关闭pool
    # pool.close()
    # pool.join()
    # print(res.get())
    # imap 按列表顺序
    # imap_unordered 按执行完的顺序
    for i in pool.imap_unordered(get_html, range(10)):
        print(f'process {i} susses')
