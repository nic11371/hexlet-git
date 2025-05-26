from telethon import TelegramClient, events, sync, connection


api_id = 26102772
api_hash = '54a0b7d2b93fb51c50807d85e18ecd40'

client = TelegramClient('session_name', api_id, api_hash, system_version="4.10.5 beta x64")
client.start()
print(client.get_me())
# client.disconnect()