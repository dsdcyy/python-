import socket
from urllib.parse import urlparse
from 装饰器.无参装饰器 import outer


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


if __name__ == '__main__':
    get_url('http://www.baidu.com')
