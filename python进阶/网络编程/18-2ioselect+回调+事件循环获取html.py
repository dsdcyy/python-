import socket
# from time import sleep
from urllib.parse import urlparse
from 装饰器.无参装饰器 import outer
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

# 实例化selector
selector = DefaultSelector()
urls = ['http://www.baidu.com']
stop = False


# DefaultSelector 根据使用平台自动选用select+poll或者epoll

# 使用select完成网络请求

class Fetcher:
    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b''
        if self.path == '':
            self.path = '/'
            # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 把状态改为无阻塞
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
            # 无法立即完成一个非阻塞套接字操作
        except BlockingIOError:
            pass
        # socket注册到selelct
        # fileobj:self.client.fileno() socket的文件描述符
        # event:事件 EVENT_READ 读事件, EVENT_WRITE 写事件
        # data:回调函数
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)
        # 处理写事件函数

    def connected(self, key):
        # 发送请求前需要取消掉监控事件
        # key.fd 注册时的socket文件描述符
        selector.unregister(key.fd)
        # 发送请求
        self.client.send(
            'GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(self.path, self.host).encode('utf8'))
        # 接收数据
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        # 服务器返回
        d = self.client.recv(1024)
        # print(d)
        if d:
            self.data += d
        # 如果数据读完了就直接停止注册
        else:
            selector.unregister(key.fd)
            data = self.data.decode('utf-8')
            # 去除头部信息
            data = data.split('\r\n\r\n')[1]
            print(data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True


# 事件循环，不停的请求socket的状态并调用对应的回调函数
def loop():
    # select本身是不支持register模式
    # socket状态变化以后的回调是由程序员完成的
    while not stop:
        res = selector.select()
        for key, mask in res:
            # key.data 找到注册时使用的方法
            call_back = key.data
            # 拿到方法后将key作为参数进行调用
            call_back(key)


@outer
# 主函数
def main():
    # 首先声明一个fetcher
    # fetcher = Fetcher()
    for i in range(2):
        # sleep(0.1)
        url = 'http://www.baidu.com'
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)

    loop()


if __name__ == '__main__':
    main()
