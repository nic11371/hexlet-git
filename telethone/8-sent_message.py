from telethon import TelegramClient, events, sync, connection
import os


api_id = 26102772
api_hash = '54a0b7d2b93fb51c50807d85e18ecd40'

result = []
with TelegramClient('my', api_id, api_hash, system_version="4.10.5 beta x64") as client:
    client.send_message('@cwadventure', 'test')
    