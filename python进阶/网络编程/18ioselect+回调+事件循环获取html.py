import socket
from urllib.parse import urlparse
from 装饰器.无参装饰器 import outer


# 使用非阻塞io完成网络请求
@outer
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
    # 设置非阻塞
    client.setblocking(False)
    try:
        client.connect((host, 80))
    # 无法立即完成一个非阻塞套接字操作
    except BlockingIOError:
        pass
    # 发送请求
    while True:
        # 不停尝试发送请求，成功则立即跳出循环
        try:
            client.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(path, host).encode('utf8'))
            break
        # 没有连接上直接跳出本次循环
        except BlockingIOError:
            continue
    data = b''
    while True:
        try:
            # 等待服务器返回
            d = client.recv(1024)
        except BlockingIOError:
            continue
        if d:
            data += d
        else:
            break
    data = data.decode('utf-8')
    # 去除头部信息
    data = data.split('\r\n\r\n')[1]
    print(data)
    client.close()


if __name__ == '__main__':
    get_url('http://www.baidu.com')
