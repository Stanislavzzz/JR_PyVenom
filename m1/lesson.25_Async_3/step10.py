import asyncio


async def get_items():
    items = ['Bob', 'Ann', 'Mary']
    print('Старт get_items')
    for item in items:
        print(f'Старт get_items - {item}')
        await asyncio.sleep(3)
        yield item


async def ticker():
    for i in range(10):
        print('Работает другая задача')
        await asyncio.sleep(1)


async def main():
    print('Старт')
    task = asyncio.create_task(ticker())

    async for name in get_items():
        print(f'Имя - {name}')

    await task

    
asyncio.run(main())