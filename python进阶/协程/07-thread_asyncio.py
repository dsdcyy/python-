# 使用多线程：在协程中继承阻塞io
import asyncio
import socket
from urllib.parse import urlparse
from 装饰器.无参装饰器 import outer
from concurrent.futures import ThreadPoolExecutor


def get_url(url):
    # 解析url
    url = urlparse(url)
    # 获得主域名
    host = url.netloc
    # 获得子路经
    path = url.path
    if path == '':
        path = '/'
    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))
    # 发送请求
    client.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(path, host).encode('utf8'))
    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf-8')
    # 去除头部信息
    # data = data.split('\r\n\r\n')[1]
    print(data)
    client.close()


@outer
def main():
    loop = asyncio.new_event_loop()
    execut = ThreadPoolExecutor()
    # 将某个阻塞io的函数放到线程池去运行
    # 线程池,函数，参数
    tasks = [loop.run_in_executor(execut, get_url, 'https://www.baidu.com') for i in range(20)]
    loop.run_until_complete(asyncio.gather(*tasks))


if __name__ == '__main__':
    main()
