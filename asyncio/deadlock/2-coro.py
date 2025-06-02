import asyncio


# Корутина, которая дважды получает замок
async def task(lock):
    print('Задача пытается захватить замок...')

    # Захватываем замок
    async with lock:
        print('Задача снова пытается захватить замок...')

        # Снова захватываем замок
        async with lock:
            pass


async def main():
    lock = asyncio.Lock()
    await task(lock)


asyncio.run(main())
