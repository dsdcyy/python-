import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED


def get_html(times):
    time.sleep(times)
    print(f'get page {times} successfully')
    return times


if __name__ == '__main__':
    urls = [0.2, 0.4, 0.6, 0.8, 1]
    # 创建线程池
    executor = ThreadPoolExecutor(max_workers=2)
    # 判断任务是否成功
    # 方法1
    tasks = [executor.submit(get_html, url) for url in urls]
    # as_completed 判断一个任务队列的任务执行成功的任务
    # 遍历.result 获得函数的返回值
    tasks_completed = [i.result() for i in as_completed(tasks)]
    # 等待tasks执行结束,return_when FIRST_COMPLETED 传入的列表的第一函数执行完就停止等待
    wait(tasks, return_when=FIRST_COMPLETED)
    print(tasks_completed)
    # 方法2
    # executor.map 判断执行成功的函数并获得返回值
    tasks2 = [i for i in executor.map(get_html, urls)]
    print(tasks2)
    # # submit 提交执行的函数到线程池中
    # # 返回值为<class 'concurrent.futures._base.Future'>类
    # task1 = executor.submit(get_html, 2)
    # task2 = executor.submit(get_html, 3)
    # # done() 判断函数是否执行成功
    # print(task1.done(), type(task1))
    # # 取消任务，如果成功返回true，如果已经在执行则无法取消该任务，返回false
    # print(task2.cancel())
    # print(task2.done())
    # # 获取函数执行返回结果阻塞方法
    # print(task1.result())
