from telethon import TelegramClient, events, sync, connection
from telethon.tl.functions.users import GetFullUserRequest


api_id = 26102772
api_hash = '54a0b7d2b93fb51c50807d85e18ecd40'

with TelegramClient('my', api_id, api_hash, system_version="4.10.5 beta x64") as client:
    all_message = client.get_messages(
        'https://t.me/Parsinger_Telethon_Test',
        limit=None
        )
    for message in all_message:
        if message.pinned:
            print(message.from_id.user_id)
