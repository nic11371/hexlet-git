import asyncio

# Устанавливаем начальный баланс
balance = 100

# Создаем объект lock для синхронизации
lock = asyncio.Lock()


# Определяем асинхронную функцию пополнения счета
async def deposit(amount):
    global balance
    # Используем lock, чтобы защитить доступ к переменной balance
    async with lock:
        print(f"Баланс пополнен на {amount} у.е.")
        balance += amount
        print(f"Текущий баланс {balance}")


# Определяем асинхронную функцию снятия средств
async def withdraw(amount):
    global balance
    # Используем lock, чтобы защитить доступ к переменной balance
    async with lock:
        if balance >= amount:
            print(f"Снятие {amount} у.е.")
            balance -= amount
            print(f"Текущий баланс {balance}")
        else:
            print(f"Попытка снять {amount}, недостаточно средств, текущий баланс {balance} у.е.")


async def main():
    task1 = asyncio.create_task(deposit(50))
    task2 = asyncio.create_task(withdraw(200))
    await task1
    await task2

asyncio.run(main())
