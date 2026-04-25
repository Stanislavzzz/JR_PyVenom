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
        "https://jsonplaceholder.typicode.com/comments",
    ]
    async with aiohttp.ClientSession() as session:
        users_task = asyncio.create_task(fetch_data(session, urls[0]))
        posts_task = asyncio.create_task(fetch_data(session, urls[1]))
        users, posts = await asyncio.gather(users_task, posts_task)

        print(f"Пользователей: {len(users)}")
        print(f"Постов: {len(posts)}")


asyncio.run(main())