import asyncio
from asyncio import LifoQueue


async def autosave(queue):
    for time in range(1, 21):
        print(f"Автосохранение игры через {time} часов")
        await queue.put(time)
        await asyncio.sleep(.1)


async def simulate_gameplay(queue):
    while True:
        await asyncio.sleep(.1)
        time = await queue.get()
        if time % 5 == 0:
            print(f"Загружена последняя версия игры: Автосохранение {time}")
        queue.task_done()


async def main():
    queue = LifoQueue()
    save_task = asyncio.create_task(autosave(queue))
    asyncio.create_task(simulate_gameplay(queue))
    await save_task
    await queue.join()
    print('Игра пройдена!')


asyncio.run(main())
