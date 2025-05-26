from telethon import TelegramClient, events, sync, connection
import asyncio
import os


api_id = 26102772
api_hash = '54a0b7d2b93fb51c50807d85e18ecd40'

client = TelegramClient('session_name', api_id, api_hash, system_version="4.10.5 beta x64")
client.start()
print(client.get_me())
# client.disconnect()

participants = client.get_participants('https://t.me/Parsinger_Telethon_Test')
for i, user in enumerate(participants):
    client.download_profile_photo(user, f'{i}', download_big=False)
    print(user.id, user.first_name, user.last_name, user.phone)

def get_size(folder: str):
    return sum(
        [os.path.getsize(f"{folder}/{file}") for file in os.listdir(folder)]
    )

get_size('C:/Users/melnikov.nn/Documents/phyton/Lessons/2-hexlet-git/telethone')