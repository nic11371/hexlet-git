import asyncio


async def coro():
    await asyncio.sleep(1)

    # Вариант 1. Без аргументов.
    raise FileNotFoundError

    # Вариант 2. Самостоятельно определяем текст сообщения.
    # raise FileNotFoundError("Файл не найден")

    # Вариант 3. Exception выбрасывается самим интерпретатором.
    # with open('bug.txt', 'r', encoding='utf-8') as file:
    #     ...


async def main():
    try:
        async with asyncio.TaskGroup() as group:
            # Создание группы задач
            [group.create_task(coro()) for _ in range(3)]
    except* FileNotFoundError as e:
        print("Исключения были перехвачены:")
        for error in e.exceptions:
            print(f"Тип ошибки: {type(error)}")
            print(f"Сообщение ошибки: {str(error)}")
            print(f"Аргументы ошибки: {error.args}")  # Аргументы исключения


asyncio.run(main())