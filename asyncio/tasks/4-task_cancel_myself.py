import asyncio

reports = [
    {"name": "Алексей Иванов", "report": "Отчет о прибылях и убытках", "load_time": 5},
    {"name": "Мария Петрова", "report": "Прогнозирование движения денежных средств", "load_time": 4},
    {"name": "Иван Смирнов", "report": "Оценка инвестиционных рисков", "load_time": 3},
    {"name": "Елена Кузнецова", "report": "Обзор операционных расходов", "load_time": 2},
    {"name": "Дмитрий Орлов", "report": "Анализ доходности активов", "load_time": 10}
]

async def download_data(report):
    current_task = asyncio.current_task()
    report_name = report.get("report")
    name = report.get("name")
    load = report.get("load_time")
    await asyncio.sleep(load)
    if name == "Дмитрий Орлов":
        cancel_task(current_task)
        print(f"Загрузка отчета {report_name} для пользователя {name} остановлена. Введите новые данные")
    print(f"Отчет: {report_name} для пользователя {name} готов")

async def cancel_task(task):
    task.cancel()

async def main():
    tasks = []
    try:
        for report in reports:
            task = asyncio.create_task(download_data(report))
            tasks.append(task)
        await asyncio.gather(*tasks)
    except asyncio.CancelledError as e:
        print(e)


asyncio.run(main())