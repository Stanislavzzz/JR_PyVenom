import asyncio


async def main():
    loop = asyncio.get_running_loop()
    # print(loop)

    future = loop.create_future()
    # print(type(future))
    print('Future сразу после создания')
    print(future)

    future.set_result('Оплата подтверждена')
    print('Future после set_result')
    print(future)

asyncio.run(main())