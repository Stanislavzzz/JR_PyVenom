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


async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/users",
        "https://jsonplaceholder.typicode.com/posts",
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_data(session, url)) for url in urls]

        results = await asyncio.gather(*tasks)

        for result in results:
            print(f"Кол-во элементов: {len(result)}")

asyncio.run(main())