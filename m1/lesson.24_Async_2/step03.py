import asyncio


async def main():
    loop = asyncio.get_running_loop()
    print(type(loop))
    print(loop)

    future = loop.create_future()
    print(type(future))
    print(future)


asyncio.run(main())