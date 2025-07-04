import asyncio


patient_info = [
    "Алексей Иванов: Прием для общего осмотра",
    "Мария Петрова: Чистка зубов",
    "Ирина Сидорова: Анализ крови",
    "Владимир Кузнецов: Рентгеновское исследование",
    "Елена Васильева: Вакцинация",
    "Дмитрий Николаев: Выписка рецепта",
    "Светлана Михайлова: Осмотр офтальмолога",
    "Никита Алексеев: Сеанс физиотерапии",
    "Ольга Сергеева: Срочный прием",
    "Анна Жукова: Регулярный контрольный осмотр"
]


async def producer(queue):
    for patient in patient_info:
        await asyncio.sleep(0.5)
        await queue.put(patient)
        print(
            f"Регистратор добавил в очередь: {patient}")
    await queue.put(None)


async def consumer(queue):
    while True:
        patient = await queue.get()
        if patient is None:
            break
        print(f"Врач принял пациента: {patient}")
        await asyncio.sleep(0.5)


async def main():
    queue = asyncio.Queue()

    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())
