import asyncio
import time

async def process_order(order_id):
    print(f'Начали обработку заказа {order_id}')
    await asyncio.sleep(3)
    print(f'Завершили обработку заказа {order_id}')
    return f"Заказа {order_id} выполнен"


async def main():
    start = time.time()
    task_1 = asyncio.create_task(process_order(101))
    task_2 = asyncio.create_task(process_order(202))
    task_3 = asyncio.create_task(process_order(303))

    print(task_1)
    print(task_1)
    print(task_1)

    # print(type(task))
    result_1 = await task_1
    result_2 = await task_2
    result_3 = await task_3

    print(result_1)
    print(result_2)
    print(result_3)
    #
    # await process_order(101)
    # await process_order(102)
    # await process_order(103)

    end = time.time() - start
    print(end)

asyncio.run(main())
# asyncio.run(process_order(1))