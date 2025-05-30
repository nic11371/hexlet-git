import asyncio
import re
# Для удобства полные наборы данных вшиты в задачу, вставлять их не нужно
banned_words = ['отладку']
message = [{
    "message_id": 78228,
    "message": "Стоит ли рассмотреть отладку этого кода?"
}]


async def check_massage(message):
    id = message.get("message_id")
    mes = message.get("message")
    text_lower = mes.lower()
    current_task = asyncio.current_task()
    if any([re.search(rf"{banned_word}\W", text_lower) for banned_word in banned_words]):
        print(f"В сообщении {id} стоп-слово: task.done(): {current_task.done()}")
        current_task.cancel()
        raise asyncio.CancelledError
    await asyncio.sleep(1)
    print(f"{id}: {mes}")


async def main():
    tasks = []
    for msg in message:
        task = asyncio.create_task(check_massage(msg))
        tasks.append(task)
    try:
        await asyncio.gather(*tasks, return_exceptions=True)
    except asyncio.CancelledError as e:
        print(e)

asyncio.run(main())
