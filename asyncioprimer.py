
import asyncio
import time

async def waiter() -> None:
    tt=asyncio.create_task(cook('Паста 2', 12))    
    qw=asyncio.create_task(cook('Салат Цезарь1', 3))
    qa=asyncio.create_task(cook('Отбивные 3', 16))
    qz=asyncio.create_task(cook('fsdf 4', 33)  )

    await tt
    await qz
    await qa
    await qw
    

async def cook(order: str, time_to_prepare: int) -> None:
        print(f'Новый заказ: {order}')
        await  asyncio.sleep(time_to_prepare)
        print(order, '- готово')

asyncio.run(waiter())
