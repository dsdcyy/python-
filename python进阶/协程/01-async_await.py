# python为了将语义变得更加明确，引入了async和await关键词用于定义原生的协程
async def downloader(url):
    return 'bobby'


# async => asyncio.coroutine
async def download_url(url):
    # await => yield from
    html = await downloader(url)
    return html


if __name__ == '__main__':
    coro = download_url('https://www.imooc.com')
    coro.send(None)
