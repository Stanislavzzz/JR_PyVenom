def say_hello():
    return "Hello World! Синхронный"


async def say_hello_async():
    return "Hello World! Асинхронный"


if __name__ == '__main__':

    # result = say_hello()
    # print(result)

    result = say_hello_async()
    print(result)
    print(type(result))