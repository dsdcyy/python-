# Semaphore 用于控制进入数量的锁
# 文件,读,写 ，写一般只是用一个线程写，读可以用多个线程
import threading
import time


class Get_html_tex(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(0.5)
        print(f'get {self.url} text successfully!')
        # 释放锁Semaphore.value +1
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            # 每循环一次Semaphore.value-1
            self.sem.acquire()
            html_thread = Get_html_tex('https://www.baidu.com/{i}'.format(i=i), sem)
            html_thread.start()


if __name__ == '__main__':
    # 限制每次并发的数量
    sem = threading.Semaphore(3)
    url_thread = UrlProducer(sem)
    url_thread.start()
