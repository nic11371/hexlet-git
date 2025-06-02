import asyncio


# Корутина, которая ждет сама себя
async def coro():
    print("Ожидает сама себя")
    await asyncio.sleep(1)
    await coro()

asyncio.run(coro())
