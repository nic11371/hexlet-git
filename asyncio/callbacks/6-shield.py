import asyncio

# Время доставки до разных городов: 
delivery_times = {
    'Москва': 1,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 4,
    'Челябинск': 6,
    'Омск': 7,
    'Красноярск': 8,
    'Владивосток': 9,
    'Хабаровск': 9
}

# Заказы:
# orders = [(подарок, город, пометка)]

# Время до нового года:
# days_left = здесь словарь город:время доставки

# Тут пишите ваш код:


async def deliver(order):
    item, city, label = order
    delay = int(delivery_times.get(city))
    try:
        await asyncio.sleep(delay)
        print(f'Подарок {item} успешно доставлен в г. {city}')
    except asyncio.CancelledError:
        pass


async def main():
    tasks = []
    for order in orders:
        if order[2] == 'важно':
            task = asyncio.shield(deliver(order))
        else:
            task = asyncio.create_task(deliver(order))   
        tasks.append(task)
    done, pending = await asyncio.wait(tasks, timeout=days_left)

    for task in pending:
        task.cancel()

    results = await asyncio.gather(*[task for task in asyncio.all_tasks() if task.get_name() != 'Task-1'])
asyncio.run(main())