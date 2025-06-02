import asyncio

# Библиотечный каталог
library_catalog = {
    "Мастер и Маргарита": 5,
    "Война и мир": 3,
    "Преступление и наказание": 2,
    "Анна Каренина": 4,
    "Отцы и дети": 2,
    "Белые ночи": 1,
    "Кому на Руси жить хорошо": 1,
}

# Резервирование книг для пользователей
reservation_tasks = {
    "Алексей": "Мастер и Маргарита",
    "Ирина": "Мастер и Маргарита",
    "Сергей": "Война и мир",
    "Елена": "Преступление и наказание",
    "Анна": "Мастер и Маргарита",
    "Игорь": "Война и мир",
    "Мария": "Преступление и наказание",
    "Олег": "Анна Каренина",
    "Юлия": "Белые ночи",
    "Дмитрий": "Отцы и дети",
    "Татьяна": "Кому на Руси жить хорошо",
    "Светлана": "Анна Каренина",
    "Владимир": "Белые ночи",
    "Марина": "Кому на Руси жить хорошо",
    "Иван": "Анна Каренина",
}

lock = asyncio.Lock()


async def reserve_book(user_name, book_title):
    async with lock:    
        leave_books = library_catalog.get(book_title)
        if leave_books > 0:
            await asyncio.sleep(0.1)
            print(f"Пользователь {user_name} успешно зарезервировал книгу '{book_title}'.")
            library_catalog[book_title] -= 1
        else:
            print(f"Книга '{book_title}' отсутствует на складе. Резервирование для пользователя {user_name} отменено.")


async def main():
    tasks = []
    for user, book in reservation_tasks.items():
        task = asyncio.create_task(reserve_book(user, book))
        tasks.append(task)
    await asyncio.gather(*tasks)


asyncio.run(main())
