from telethon import TelegramClient, events, sync, connection
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputMessagesFilterPhotos

api_id = 26102772
api_hash = '54a0b7d2b93fb51c50807d85e18ecd40'


with TelegramClient('my', api_id, api_hash, system_version="4.10.5 beta x64") as client:
    all_message = client.get_messages(
        'https://t.me/Parsinger_Telethon_Test',
        limit=None
        )
    string = []
    for message in all_message:
        if message.message is not None and message.message.isdigit():
            string.append(int(message.message))
    print(sum(string))
