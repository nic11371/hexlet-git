import asyncio


async def task(number, locks):
    # Определяем порядок захвата блокировок по их идентификаторам
    sorted_locks = sorted(locks, key=id)
    # sorted_locks = [*locks]

    print(f"Задача {number}: пытается захватить блокировки в порядке {sorted_locks}")
    async with sorted_locks[0]:
        await asyncio.sleep(1)  # Имитация работы в критическом участке
        async with sorted_locks[1]:
            print(f"Задача {number}: захватила обе блокировки")
            await asyncio.sleep(1)  # Имитация работы в критическом участке
    print(f"Задача {number}: завершила выполнение")


async def main():
    # Инициализация двух асинхронных блокировок
    lock1 = asyncio.Lock()
    lock2 = asyncio.Lock()

    # Запуск корутин с блокировками, передаваемыми в разном порядке, но захватывающимися в одном и том же порядке
    await asyncio.gather(
        task(1, [lock1, lock2]),
        task(2, [lock2, lock1]),
    )

asyncio.run(main())

# import asyncio


# async def task(number, first_lock, second_lock):
#     print(f"Задача {number}: пытается захватить первую блокировку")
#     async with first_lock:
#         print(f"Задача {number}: захватила первую блокировку {first_lock.name}")
#         await asyncio.sleep(.1)  # Имитация работы в критическом участке
#         print(f"Задача {number}: пытается захватить вторую блокировку {second_lock.name}")

#         async with second_lock:
#             print(f"Задача {number}: захватила вторую блокировку {second_lock.name}")
#             await asyncio.sleep(.1)  # Дополнительная работа в критическом участке
#     print(f"Задача {number}: завершила выполнение")


# async def main():
#     # Инициализация двух асинхронных блокировок
#     lock1 = asyncio.Lock()
#     lock1.name = "lock1"
#     lock2 = asyncio.Lock()
#     lock2.name = "lock2"

#     # Запуск корутин с блокировками в разном порядке
#     await asyncio.gather(
#         task(1, lock1, lock2),
#         task(2, lock2, lock1),
#     )


# asyncio.run(main())
