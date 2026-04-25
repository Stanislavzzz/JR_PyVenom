import asyncio


async def load_data():
    await asyncio.sleep(3)
    return "Данные получены"


async def main():
    task = asyncio.create_task(load_data())
    result = await task
    print(result)


asyncio.run(main())