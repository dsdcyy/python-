import aiohttp
import asyncio
import aiomysql
import re
from pyquery import PyQuery
from lxml import etree

wait_urls = []
seen_urls = set()
start_url = 'https://xchina.xyz/photos/kind-2/1.html'
"""
    https://img.xchina.pics/photos/6383d7aa421f8/0002.jpg
    https://img2.xchina.pics/photos/6383d7aa421f8/0002.jpg
    
"""
match_url = re.compile(r'https://img\d?.xchina.pics/photos/\w+/\d{4,}\.\w{3,4}')

# 限制并发数量
sem = asyncio.Semaphore(6)


def make_safe_file(string: str):
    return ''.join(re.split(r'[\\/:*?"<>|"><\']', string))


def test(num):
    x_list = []
    for i in range(1, num + 1):
        j = str(i)
        if i < 10:
            x_list.append('000' + j)
        elif i < 100:
            x_list.append('00' + j)
        elif i < 1000:
            x_list.append('0' + j)
        else:
            x_list.append(j)
    return x_list


class Aiohttp(object):
    def __init__(self, __loop, __start_url, db_passwd, db_db, db_table, db_host='127.0.01', db_port=3306,
                 db_user='root'):
        self.start_url = __start_url
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_passwd = db_passwd
        self.db_db = db_db
        self.db_table = db_table
        self.pool = aiomysql.create_pool(host=db_host, port=db_port,
                                         user=db_user, password=db_passwd, db=db_db,
                                         loop=__loop, charset='utf8mb4', autocommit=True)

    @staticmethod
    async def fetch(url, session):
        async with sem:
            await asyncio.sleep(1)
            # 获取异步请求的返回对象
            if url.startswith('http'):
                print('符合url要求')
                async with session.get(url) as response:
                    try:
                        # response.status 状态码
                        print("Status:", response.status)
                        print("Content-type:", response.headers['content-type'])
                        html = await response.text()
                        if response.status in [200, 201]:
                            print("Body:", html[:20], "...")
                        return html
                    except Exception as e:
                        print('Error:', e)
                    print("Fetched")

    # 解析网址里面的a连接
    @staticmethod
    def extract_urls(html):
        urls = []
        alts = []
        print('Extracted')
        pq = PyQuery(html)
        tree = etree.HTML(html)
        img_nums = tree.xpath('//div[@class="list"]//div[@class="tag"]/div[1]/text()')
        img_nums = list(map(int, [i[:i.index('P')] for i in img_nums]))
        for link in pq('.item>a').items():
            url, alt = 'https://xchina.xyz' + link.attr('href'), link('img').attr('alt')
            if url is None:
                continue
            urls.append(url)
            alts.append(alt)
        print(urls, alts, sep='\n')
        print('extract_urls finished')
        return urls, alts, img_nums

    # 动态提交协程
    async def consumer(self, pool, stop=False):
        # 异步的在一个session中工作
        async with aiohttp.ClientSession() as session:
            while not stop:
                await asyncio.sleep(1)
                try:

                    print('hello!')
                    # 判断等待列表是否存在任务，没有则等待0.5s并跳出本次循环
                    if len(wait_urls) == 0:
                        await asyncio.sleep(0.5)
                        continue
                    # wait_urls抛出url交由article_handler动态处理
                    url = wait_urls.pop()
                    print("Start get url:", url)
                    if url not in seen_urls:
                        print('准备解析入库！')
                        seen_urls.add(start_url)
                        asyncio.ensure_future(self.article_handler(url, session, pool))

                        await asyncio.sleep(0.5)
                    else:
                        print('重新初始化！')
                        if url not in seen_urls:
                            asyncio.ensure_future(self.__init_urls(url, session))
                except Exception as e:
                    print(e)
                    continue

    async def __init_urls(self, url, session):
        html = await self.fetch(url, session)
        print('Initial!')
        seen_urls.add(url)
        self.extract_urls(html)

    # 获取文章详情并解析入库
    async def article_handler(self, url, session, pool):
        html = await self.fetch(url, session)
        seen_urls.add(url)
        pq = PyQuery(html)
        title = pq('title').text()
        content = url + '\n' + pq('p').text()
        content = make_safe_file(content)
        print(content)
        async with pool.acquire() as coon:
            async with coon.cursor() as cursor:
                sql = 'insert into {} (title,content) values ("{}","{}")'.format(self.db_table, title, content)
                print(sql)
                # 执行sql
                await cursor.execute(sql)


# 主函数 使用异步连接，等待执行fetch函数处理首页数据并返回结果
# 处理完首页后将地址添加到专门处理解析完后的链接的集合seen_urls中
# 执行extract_urls函数，将fetch函数的处理结果通过pyquery处理，拿到符合条件的url地址，将包含链接的list对象返回
# 执行consumer，它会
async def main(__loop):
    # 获取aiohttp对象
    ah = Aiohttp(__loop, start_url, '12344321', 'aiomysql_test', 'artcile')
    pool = await ah.pool
    # 等待mysql建立连接

    print("Starting")
    async with aiohttp.ClientSession() as session:
        html = await ah.fetch(start_url, session)
        ah.extract_urls(html)
    # asyncio.ensure_future(ah.consumer(pool))
    # await asyncio.gather(sem3)
    # end_loop(loop)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    # 运行主函数
    loop.run_forever()
    # asyncio.run(main(loop))
