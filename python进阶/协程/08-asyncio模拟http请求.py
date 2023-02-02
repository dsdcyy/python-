# 使用多线程：在协程中继承阻塞io
import asyncio
from urllib.parse import urlparse
from 装饰器.无参装饰器 import outer


async def get_url(url):
    # 解析url
    url = urlparse(url)
    # 获得主域名
    host = url.netloc
    # 获得子路经
    path = url.path
    if path == '':
        path = '/'

    # 建立socket连接
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(path, host).encode('utf8'))
    all_lines = [line.decode('utf8') async for line in reader]
    html = '\n'.join(all_lines)
    # print(html)
    return html


async def get_res():
    # 将协程对象转换为future对象,result拿到协程函数返回值
    tasks = [asyncio.ensure_future(get_url('http://www.baidu.com')) for i in range(2)]
    # asyncio.as_completed拿到执行完的task
    for i in asyncio.as_completed(tasks):
        result = await i
        print(result)


@outer
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete((get_res()))


if __name__ == '__main__':
    main()
