import asyncio


position = 0
count = 0
lock = asyncio.Lock()
robot_names = ['Электра', 'Механикс', 'Оптимус', 'Симулакр', 'Футуриус']


async def robot(name, number):
    global count
    async with lock:
        print(f"Робот {name}({number}) передвигается к месту A")


async def achieve(name, number):
    global count
    async with lock:
        count += 1
        print(f"Робот {name}({number}) достиг места A. Место A посещено {count} раз")


async def main():
    tasks = []
    for i, r in enumerate(robot_names):
        task_1 = asyncio.create_task(robot(r, i))
        task_2 = asyncio.create_task(achieve(r, i))
        tasks.extend([task_1, task_2])
    await asyncio.gather(*tasks)


asyncio.run(main())
