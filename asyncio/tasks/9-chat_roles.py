import asyncio
import re
# Для удобства полные наборы данных вшиты в задачу, вставлять их не нужно
banned_words = ["bug", "error", "exception", "fail", "crash", "hang", "slow", "memory leak", "infinite loop",
                "deadlock"]
message = [
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


async def check_message(mes):
    text = mes.lower()
    words = text.split(' ')
    is_flag = False
    await asyncio.sleep(1)
    for i in range(len(words)):
        word_clean = words[i].strip('.,!?;:"\'()[]{}')

        for banned_word in banned_words:
            if word_clean.lower() == banned_word.lower():
                is_flag = True
                words[i] = words[i].replace(word_clean, '***')
                break
    return ' '.join(words), is_flag


async def check_role(message):
    current_task = asyncio.current_task()
    name = current_task.get_name()
    mes = message.get("message")
    msg, flag = await check_message(mes)
    dictionary_roles = {
        'admin': mes,
        'moderator': msg,
        'student': "В сообщении есть запрещённое слово, сообщение скрыто" if flag else msg,
        'black_list_user': "Пользователь забанен, сообщение скрыто",
        "None": "ERROR_USER_NONE"
    }
    await asyncio.sleep(1)
    print(f"{name}: {dictionary_roles.get(name)}")


async def main():
    tasks = []
    for msg in message:
        role = msg.get('role')
        task = asyncio.create_task(check_role(msg), name=role)
        tasks.append(task)
    try:
        await asyncio.gather(*tasks, return_exceptions=True)
    except asyncio.CancelledError as e:
        print(e)

asyncio.run(main())
