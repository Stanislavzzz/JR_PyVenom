import asyncio
import time


async def process_order(order_id, wait_time):
    print(f'Начали обработку заказа {order_id}')

    loop = asyncio.get_running_loop()
    print(loop)

    future = loop.create_future()
    print(type(future))
    print('Future сразу после создания')
    print(future)

    print(f"Заказ {order_id=}: Начали обработку: ")
    await asyncio.sleep(wait_time)
    future.set_result(f'Оплата {order_id=}  подтверждена')
    result = await future
    print(f'Завершили обработку заказа {order_id}')
    return result


async def main():
    start = time.time()
    task_1 = asyncio.create_task(process_order(101, 3))
    print(task_1)

    print(f"Задача завершена? {task_1.done()=}")
    result_main = await task_1
    print(f"Задача завершена? {task_1.done()=}")
    print(f"Результат задачи:  {task_1.result()=}")
    print(f'Итоговой результат {result_main=}')

    end = time.time() - start
    print(end)


asyncio.run(main())