from pyrogram import Client


api_id = 26102772
api_hash = '54a0b7d2b93fb51c50807d85e18ecd40'
group_url = "parsinger_pyrogram"
app = Client("my_session", api_id=api_id, api_hash=api_hash)
app.start()


app = Client(
    "my_account",  # Имя сессии
    api_id=12345,   # Получить на my.telegram.org
    api_hash="abcdef123456"  # Получить там же
)


async def main():
    async with app:
        print(await app.get_me())  # Проверка подключения

app.run(main())  # Запуск асинхронного кода
