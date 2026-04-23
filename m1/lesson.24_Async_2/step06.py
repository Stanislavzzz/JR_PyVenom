import asyncio


async def main():
    loop = asyncio.get_running_loop()
    # print(loop)

    future = loop.create_future()
    # print(type(future))
    print('Future сразу после создания')
    print(future)

    # future.set_result('Оплата подтверждена')
    future.set_exception(ValueError('Оплата  не прошла '))
    print('Future после set_exception')
    print(future)
    print('*' * 50)
    try:
        result = await future
        print(f"Результат Future:  {result=}")
    except ValueError as e:
        print(f'Поймали  ошибку Future: {e}')


asyncio.run(main())