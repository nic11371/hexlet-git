import asyncio

files = ['image.png', 'file.csv', 'file1.txt' 
# missed_files = [...] список пропущенных файлов "спрятан" внутри задачи

# Не менять функцию
async def download_file(file_name):
    await asyncio.sleep(1)
    if file_name in missed_files:
        raise FileNotFoundError(f'Файл {file_name} не найден')
    else:
        await asyncio.sleep(1)
        return f'Файл {file_name} успешно скачан'

# Ваш код пишите тут:    
async def main():
    tasks = []
    for file in files:
        task = asyncio.create_task(download_file(file))
        tasks.append(task)
    try:
        await asyncio.gather(*tasks, return_exceptions=True)
    except FileNotFoundError as e:
        print(e)
    for task in tasks:
        exception = task.exception()
        if exception:
            print(exception)


asyncio.run(main())