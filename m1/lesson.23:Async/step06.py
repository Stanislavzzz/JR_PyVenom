import asyncio
import time


async def process_order(order_id, wait_time):
    print(f'Начали обработку заказа {order_id}')
    await asyncio.sleep(wait_time)
    print(f'Завершили обработку заказа {order_id}')
    return f"Заказа {order_id} выполнен"


async def main():
    start = time.time()
    task_1 = asyncio.create_task(process_order(101, 3))
    print(f'Сразу после создания {task_1.done()=}')

    await task_1
    print(f'После await task_1 {task_1.done()=}')

    print(f'Результат task_1 {task_1.result()=}')
    print(f'Исключения task_1 {task_1.exception()=}')


    end = time.time() - start
    print(end)

asyncio.run(main())
# asyncio.run(process_order(1))