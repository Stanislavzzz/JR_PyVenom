import asyncio
import aiohttp


async def fetch_data():
    async with aiohttp.ClientSession() as session:
        # async with session.get("http://httpbin.org/get") as response:
        async with session.get("https://jsonplaceholder.typicode.com/users") as response:
            status_code = response.status
            print(f"Status code: {status_code}")
            text = await response.text()
            print(text[:300])
            print(type(text))

            json_data = await response.json()
            print(json_data)
            print(type(json_data))
            print(json_data[0])
            print(type(json_data[0]))


async def main():
    await fetch_data()


asyncio.run(main())