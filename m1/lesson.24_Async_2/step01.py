# task.add_done_callback()

import asyncio
import time


async def process_order(order_id, wait_time):
    print(f'Начали обработку заказа {order_id}')
    await asyncio.sleep(wait_time)
    print(f'Завершили обработку заказа {order_id}')
    return f"Заказа {order_id} выполнен"


def on_task_done(task):
    print('Callback: Задача завершилась.')
    print(f'Результат task {task.result()=}')


async def main():
    start = time.time()
    task_1 = asyncio.create_task(process_order(101, 3))
    print(task_1)
    task_1.add_done_callback(on_task_done)

    await task_1

    end = time.time() - start
    print(end)


asyncio.run(main())