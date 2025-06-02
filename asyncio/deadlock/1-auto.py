import asyncio


async def car(lock1, lock2, name):
    print(f'Автомобиль {name} приближается к перекрестку.')
    await asyncio.sleep(1)  # Имитация времени приближения к перекрестку

    async with lock1:
        print(f'Автомобиль {name} ожидает на перекрестке.')
        await asyncio.sleep(1)  # Имитация времени ожидания на перекрестке

        async with lock2:
            # В реальной ситуации этот код никогда не выполнится из-за deadlock
            print(f'Автомобиль {name} покидает перекресток.')


async def main():
    # Инициализация замков для каждого "направления" движения
    north_south = asyncio.Lock()
    east_west = asyncio.Lock()

    # Запуск асинхронных задач для каждого автомобиля
    await asyncio.gather(
        car(north_south, east_west, 'Север-Юг'),
        car(east_west, north_south, 'Восток-Запад'),
        car(north_south, east_west, 'Юг-Север'),
        car(east_west, north_south, 'Запад-Восток')
    )


asyncio.run(main())
