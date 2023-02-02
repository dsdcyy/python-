import asyncio


async def work(sem):
    async with sem:
        print('Working!')
        await asyncio.sleep(2)


async def main():
    sem = asyncio.Semaphore(3)
    await asyncio.gather(work(sem), work(sem), work(sem))
if __name__ == '__main__':
    asyncio.run(main())