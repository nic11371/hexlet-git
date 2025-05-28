import asyncio
import random


async def prepare_pizza():      
    print("Готовим пиццу...")
    await asyncio.sleep(5)      
    return "Пицца готова!"


def notify_delivery(task):  # Callback-функция для уведомления о доставке пиццы
    print("Курьер: Ваш заказ доставлен!")


def cancel_notification(task):  # Callback-функция для отмены уведомления о доставке
    print("Курьер: Уведомление отменено, заберите пиццу самостоятельно.")


async def main():                              
    task = asyncio.create_task(prepare_pizza())   
    
    # Регистрация callback-функций
    task.add_done_callback(notify_delivery)             
    task.add_done_callback(cancel_notification)

    if random.choice([True, False]):                    
        print('Доставка подтверждена, везём пиццу') 
        task.remove_done_callback(cancel_notification)  # Отмена уведомления об отмене доставки
    else:
        print('Доставка отменена, самовывоз') 
        task.remove_done_callback(notify_delivery)      # Отмена уведомления о доставке
    
    await task


asyncio.run(main())