import asyncio
import time


async def process_order(order_id, wait_time):
    print(f'Начали обработку заказа {order_id}')
    try:
        await asyncio.sleep(wait_time)

        return f"Заказа {order_id} выполнен"
    except asyncio.CancelledError:
        print(f'Отменили обработку заказа {order_id}')
        raise


async def main():
    start = time.time()
    # cancel()
    task_1 = asyncio.create_task(process_order(101, 10))

    await asyncio.sleep(3)

    print(f'Отменяем нашу задачу с заказом')
    task_1.cancel()

    try:
        await task_1
    except asyncio.CancelledError:
        print('Снаружи - подтверждаем, что задача отменена')

    # task_2 = asyncio.create_task(process_order(202, 1))
    # task_3 = asyncio.create_task(process_order(303, 2))
    #
    # print(task_1)
    # print(task_1)
    # print(task_1)

    # wait()
    # done
    # pending

    # done, pending = await asyncio.wait([task_1, task_3, task_2], timeout=1.5)
    # # result = await asyncio.gather(task_1, task_3, task_2)
    # # print(type(result))
    #
    # print("Задачи DONE: ")
    # print(done)
    #
    # print("Задачи PENDING: ")
    # print(pending)

    end = time.time() - start
    print(end)

asyncio.run(main())
# asyncio.run(process_order(1))