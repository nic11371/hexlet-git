import asyncio

# Общий ресурс, который будет обновляться
shared_resource = 0
lock = asyncio.Lock()

async def update_resource():

    # Используем глобальную переменную shared_resource
    global shared_resource
    print('Начинаем обновление shared_resource')
    
    # Сохраняем текущее значение shared_resource во временную переменную
    async with lock:
        temp = shared_resource

    # Имитация операции ввода-вывода
        await asyncio.sleep(1)  

    # Увеличиваем значение shared_resource на 1
        shared_resource = temp + 1
    print('Обновление shared_resource завершено')


async def main():
    await asyncio.gather(update_resource(), update_resource(), update_resource())
    print(f'shared_resource: {shared_resource}')

asyncio.run(main())