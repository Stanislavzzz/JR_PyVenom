import asyncio


async def get_items():
    items = ['Bob', 'Ann', 'Mary']
    print('Старт get_items')
    for item in items:
        print(f'Старт get_items - {item}')
        await asyncio.sleep(3)
        yield item


async def main():
    print('Старт')
    async for name in get_items():
        print(f'Имя - {name}')

asyncio.run(main())