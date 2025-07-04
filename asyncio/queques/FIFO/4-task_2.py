import asyncio


patient_info = [
        {'name': 'Алексей Иванов', 'direction': 'Терапевт', 'procedure': 'Прием для общего осмотра'},
        {'name': 'Мария Петрова', 'direction': 'Хирург', 'procedure': 'Малая операция'},
        {'name': 'Ирина Сидорова', 'direction': 'ЛОР', 'procedure': 'Осмотр уха'},
        {'name': 'Владимир Кузнецов', 'direction': 'Терапевт', 'procedure': 'Консультация'},
        {'name': 'Елена Васильева', 'direction': 'Хирург', 'procedure': 'Хирургическая процедура'},
        {'name': 'Дмитрий Николаев', 'direction': 'ЛОР', 'procedure': 'Промывание носа'},
        {'name': 'Светлана Михайлова', 'direction': 'Терапевт', 'procedure': 'Рутинный осмотр'},
        {'name': 'Никита Алексеев', 'direction': 'Хирург', 'procedure': 'Операция на колене'},
        {'name': 'Ольга Сергеева', 'direction': 'ЛОР', 'procedure': 'Лечение ангины'},
        {'name': 'Анна Жукова', 'direction': 'Терапевт', 'procedure': 'Вакцинация'}
    ]


async def producer(queue, patient):
    await asyncio.sleep(0.5)
    await queue.put(patient)
    print(
        f"Регистратор добавил в очередь: {patient['name']}, направление: {patient['direction']}, процедура: {patient['procedure']}")


async def consumer(queue, doctor_type):
    while True:
        patient = await queue.get()
        print(f"{doctor_type} принял пациента: {patient['name']}, процедура: {patient['procedure']}")
        await asyncio.sleep(0.5)
        queue.task_done()


async def main():
    queue_therapy = asyncio.Queue()
    queue_surgeon = asyncio.Queue()
    queue_ent = asyncio.Queue()

    consumers = [
        asyncio.create_task(consumer(queue_therapy, "Терапевт")),
        asyncio.create_task(consumer(queue_surgeon, "Хирург")),
        asyncio.create_task(consumer(queue_ent, "ЛОР"))
    ]

    for patient in patient_info:
        if patient.get('direction') == "Терапевт":
            await producer(queue_therapy, patient)
        if patient.get('direction') == "Хирург":
            await producer(queue_surgeon, patient)
        if patient.get('direction') == "ЛОР":
            await producer(queue_ent, patient)

    await queue_therapy.join()
    await queue_surgeon.join()
    await queue_ent.join()
    for task in consumers:
        task.cancel()


asyncio.run(main())
