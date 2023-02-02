# 实例化selector
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
from urllib.parse import urlparse
import socket

selector = DefaultSelector()
urls = ['http://www.baidu.com']
stop = False


def get_socket_data():
    yield 'bobby'


def download(url):
    spider_url = url
    url = urlparse(url)
    host = url.netloc
    path = url.path
    data = b''
    if path == '':
        path = '/'
        # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 把状态改为无阻塞
    client.setblocking(False)
    try:
        client.connect((host, 80))
        # 无法立即完成一个非阻塞套接字操作
    except BlockingIOError:
        pass
    # socket注册到selelct
    # fileobj:client.fileno() socket的文件描述符
    # event:事件 EVENT_READ 读事件, EVENT_WRITE 写事件
    # data:回调函数
    selector.register(client.fileno(), EVENT_WRITE, connected)
    # 单线程模式将耗时的操作yield出去
    source = yield from get_socket_data()
    data = source.decode('utf-8')
    data = data.split('\r\n\r\n')[1]
    print(data)
    # 处理写事件函数


def download_html(html, url):
    html = yield from download(url)


def connected():
    pass


if __name__ == '__main__':
    ...
