import asyncio
import re
# Для удобства полные наборы данных вшиты в задачу, вставлять их не нужно
banned_words = ["bug", "error", "exception", "fail", "crash", "hang", "slow", "memory leak", "infinite loop",
                "deadlock"]
messages = [
    {
        "message_id": 56691,
        "message": "У тебя есть опыт работы с Node.js?",
        "role": "black_list_user"
    },
    {
        "message_id": 59368,
        "message": "Я читаю книгу о криптографии, она очень интересная.",
        "role": "admin"
    },
    {
        "message_id": 90083,
        "message": "Ты когда-нибудь работал с NoSQL базами данных?",
        "role": "None"
    },
    {
        "message_id": 26180,
        "message": "Давай попробуем разобраться с этим bug.",
        "role": "student"
    },
    {
        "message_id": 45677,
        "message": "Я думаю, мы должны рассмотреть новый алгоритм для этого задания.",
        "role": "moderator"
    },
    {
        "message_id": 15224,
        "message": "Не могу понять, в какой функции появляется этот bug.",
        "role": "moderator"
    },
]


def student(text):
    if re.findall(f'\b{banned_words}\b', text, re.I):
        return 'В сообщении есть запрещённое слово, сообщение скрыто'
    return text


async def check_message(message):
    roles = {
        'admin': message['message'],
        'moderator': re.sub(banned_words, '****', message['message']),
        'student': student(message['message']),
        'black_list_user': 'Пользователь забанен, сообщение скрыто',
        None: 'ERROR_USER_NONE'
    }
    print(f'{message["role"]}: {roles[message["role"]]}')


async def main():
    await asyncio.gather(*map(check_message, messages))

asyncio.run(main())
