import asyncio
import aiohttp


async def fetch_data(session, url):
    async with session.get(url) as response:
        status_code = response.status
        print(f"URL: {url}")
        print(f"Status code: {status_code}")

        json_data = await response.json()
        # print(json_data)
        # print(type(json_data))
        #
        return json_data


async def fetch_results(session, urls):
    for url in urls:
        data = await fetch_data(session, url)
        yield data


async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/users",
        "https://jsonplaceholder.typicode.com/posts",
    ]
    async with aiohttp.ClientSession() as session:
        async for item in fetch_results(session, urls):

            print(f"Кол-во элементов: {len(item)}")

asyncio.run(main())