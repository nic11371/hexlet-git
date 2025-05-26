import asyncio

async def process_task():
    await asyncio.sleep(1)
    return id(asyncio.current_task())

async def main():
    tasks = []
    for i in range(10):
        task = asyncio.create_task(process_task())
        tasks.append(task)
    return await asyncio.gather(*tasks)

asyncio.run(main())

