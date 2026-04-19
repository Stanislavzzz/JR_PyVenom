import asyncio
import time


async def say_hello_async():
    # start_time = time.time()
    print("Начало выполнения корутины")
    await asyncio.sleep(3)

    print("Пауза")
    await asyncio.sleep(3)

    print("Завершение выполнения корутины")
    # end_time = time.time()
    # result = end_time - start_time
    # print(result)


if __name__ == '__main__':
    asyncio.run(say_hello_async())

