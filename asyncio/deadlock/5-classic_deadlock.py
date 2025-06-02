import asyncio

async def coroutine_a(event_a, event_b):
    print("Корутина A: начата")
    await event_b.wait()  # ожидает установки события в корутине B
    print("Корутина A: ожидает корутину B")
    event_a.set()

async def coroutine_b(event_b, event_c):
    print("Корутина B: начата")
    await event_c.wait()  # ожидает установки события в корутине C
    print("Корутина B: ожидает корутину C")
    event_b.set()

async def coroutine_c(event_c, event_a):
    print("Корутина C: начата")
    await event_a.wait()  # ожидает установки события в корутине A
    print("Корутина C: ожидает корутину A")
    event_c.set()

async def main():
    # Создание событий для каждой корутины
    event_a = asyncio.Event()
    event_b = asyncio.Event()
    event_c = asyncio.Event()

    # Запуск корутин
    await asyncio.gather(
        coroutine_a(event_a, event_b),
        coroutine_b(event_b, event_c),
        coroutine_c(event_c, event_a),
    )

asyncio.run(main())
