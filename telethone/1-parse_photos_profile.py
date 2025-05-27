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
for i in participants:
    for iter_photo in client.iter_profile_photos(i):
        client.download_media(iter_photo, file='img/')

# def get_size(folder: str):
#     return sum(
#         [os.path.getsize(f"{folder}/{file}") for file in os.listdir(folder)]
#     )

# get_size('C:/Users/melnikov.nn/Documents/phyton/Lessons/2-hexlet-git/telethone')