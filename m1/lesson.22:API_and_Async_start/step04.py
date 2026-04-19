import asyncio
import time


async def say_hello_async():
    # start_time = time.time()
    print("1. Начало выполнения корутины 1")
    print("2. Будет ожидание 3 сек.")
    await asyncio.sleep(3)
    #
    print("Пауза")
    await asyncio.sleep(3)

    print("3. Ожидание Завершения выполнения корутины")
    print("4. Завершение выполнения корутины")

    # end_time = time.time()
    # result = end_time - start_time
    # print(result)


if __name__ == '__main__':
    asyncio.run(say_hello_async())

