import asyncio

files = {
    "file1.mp4": 32,
    "image2.png": 24,
    "audio3.mp3": 16,
    "document4.pdf": 8,
    "archive5.zip": 40,
    "video6.mkv": 48,
    "presentation7.pptx": 12,
    "ebook8.pdf": 20,
    "music9.mp3": 5,
    "photo10.jpg": 7,
    "script11.py": 3,
    "database12.db": 36,
    "archive13.rar": 15,
    "document14.docx": 10,
    "spreadsheet15.xls": 25,
    "image16.gif": 2,
    "audioBook17.mp3": 60,
    "tutorial18.mp4": 45,
    "code19.zip": 22,
    "profile20.jpg": 9
}
NETWORK_SPEED = 8  # MB/s

async def download_file(filename, size):
    download_time = round(size / NETWORK_SPEED, 3)
    print(f"Начинается загрузка файла: {filename}, его размер {size} мб, время загрузки составит {download_time} сек")
    await asyncio.sleep(download_time)
    print(f"Загрузка завершена: {filename}")

async def monitor_tasks(tasks):
    while True:
        all_done = True
        current_status = []
        
        for task in tasks:
            status = task.done()
            if not status:
                all_done = False
            current_status.append(f"Задача {task.get_name()}: {'завершена' if status else 'в процессе'}, Статус задачи {status}")
        
        # Выводим статус только если он изменился
        if not hasattr(monitor_tasks, 'prev_status') or monitor_tasks.prev_status != current_status:
            for status in current_status:
                print(status)
            monitor_tasks.prev_status = current_status
        
        if all_done:
            break
        
        await asyncio.sleep(1)

async def main():
    tasks = []
    for filename, size in files.items():
        task = asyncio.create_task(download_file(filename, size))
        task.set_name(filename)
        tasks.append(task)
    
    await monitor_tasks(tasks)
    print("Все файлы успешно загружены")

if __name__ == "__main__":
    asyncio.run(main())
