from telethon import TelegramClient, events, sync, connection
import os


api_id = 26102772
api_hash = '54a0b7d2b93fb51c50807d85e18ecd40'

result = []
with TelegramClient('my', api_id, api_hash, system_version="4.10.5 beta x64") as client:
    all_message = client.get_messages(
        'https://t.me/Parsinger_Telethon_Test',
        limit=None
        )
    usernames = []
    for message in all_message:
        client.download_media(message, file='img/')


def get_size(folder: str):
    return sum(
        [os.path.getsize(f"{folder}/{file}") for file in os.listdir(folder)]
    )

# get_size('img/')