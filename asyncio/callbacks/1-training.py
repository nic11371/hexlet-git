import asyncio


def notify_start_training(task):  # Callback-функция - начало тренировки
    print("Тренировка начинается, идите в спортзал.")


def cancel_training(task):  # Callback-функция - отмена тренировки
    print("Тренировка отменена.")


async def prepare_training():  # Асинхронная функция для ожидания тренировки
    await asyncio.sleep(3)


async def main(is_training_scheduled):
    task = asyncio.create_task(prepare_training())

    # Регистрация callback-функций
    task.add_done_callback(notify_start_training)       
    task.add_done_callback(cancel_training)
    
    if is_training_scheduled:                           
        task.remove_done_callback(cancel_training)  # Тренировка назначена, удаляем callback-функцию cancel_training()
    else:                                               
        task.remove_done_callback(notify_start_training)  # Тренировка отменена, удаляем callback-функцию notify_start_training()
    await task                                          

# Флаг для определения состояния тренировки:
# True - тренировка назначена
# False - тренировка отменена
asyncio.run(main(False))