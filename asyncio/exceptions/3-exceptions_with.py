import asyncio


async def coro():
    name = asyncio.current_task().get_name()
    print(f'{name} начала свою работу!')
    await asyncio.sleep(1)
    print(f'{name} завершена!')


# Корутина для подъема исключений
async def ex_coro():
    await asyncio.sleep(.5)
# 1) Поведение характерное для обработки KeyboardInterrupt и SystemExit
# Повторный вызов изначального исключения
    # print('ex_coro поднимает исключение KeyboardInterrupt')
    # raise KeyboardInterrupt
# 2) Поведение характерное для обработки других исключений (кроме asyncio.CancelledError)
# Исключения группируются в ExceptionGroup
    print('ex_coro поднимает исключение Exсeption')
    raise Exception('Что-то пошло не так!(((')


async def main():
    # Создание группы задач
    async with asyncio.TaskGroup() as group:
        # Создание трех задач
        tasks = [group.create_task(coro(), name=f'Задача_0{i}') for i in range(1, 4)]
        # Создание задачи, имитирующей возникновение исключения
        task_ex = group.create_task(ex_coro())


asyncio.run(main())