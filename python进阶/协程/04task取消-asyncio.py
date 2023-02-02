import asyncio

# loop = asyncio.get_event_loop()
# # run_forever不会停止，会一直循环
# loop.run_forever()
# # 运行了指定的协程后是会停止的 run_until_complete
# loop.run_until_complete()


# loop会放到future中
# 取消future(task)
async def get_html(sleep_times):
    print('waiting')
    await asyncio.sleep(sleep_times)
    print('done after {} seconds'.format(sleep_times))


if __name__ == '__main__':
    task1 = get_html(1)
    task2 = get_html(2)
    task3 = get_html(3)
    tasks = [task1, task2, task3]
    print('1')
    loop = asyncio.new_event_loop()
    # 旧版本使用
    # loop = asyncio.get_event_loop()
    print('2')
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.all_tasks(loop)
        for task in all_tasks:
            print('cancel task')
            # 取消task并返回布尔值判断是否取消成功
            print(task.cancel())
        loop.stop()
        # 不使用会报错 Task was destroyed but it is pending!
        loop.run_forever()
    finally:
        loop.close()
    print('3')
