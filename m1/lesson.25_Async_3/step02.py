import asyncio
import aiohttp


async def fetch_data():
    async with aiohttp.ClientSession() as session:
        # async with session.get("http://httpbin.org/get") as response:
        async with session.get("https://jsonplaceholder.typicode.com/users") as response:
            text = await response.text()
            print(text)


async def main():
    await fetch_data()


asyncio.run(main())