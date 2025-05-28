import asyncio
import time

codes = ["56FF4D", "A3D2F7", "B1C94E", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F0"]

messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!",
            "Всего наилучшего!"]


async def message(n):
    # Каждое сообщение отправляется за 1+ секунду  (последнее + 14*0.04==0.56)
    await asyncio.sleep(1 + (n * 0.04))
    print(f"Сообщение: {messages[n]}")
    await asyncio.sleep(0)

    return codes[n]


def code(task):
    print(f"Код: {task.result()}")


async def main():
    tasks = []

    for x in range(len(messages)):
        task = asyncio.create_task(message(x))
        task.add_done_callback(code)
        tasks.append(task)

    await asyncio.gather(*tasks)


# start = time.time()
asyncio.run(main())
# print(time.time() - start) # 1.5613627433776855




