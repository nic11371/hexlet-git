from telethon import TelegramClient, events, sync, connection
from telethon.tl.functions.users import GetFullUserRequest
import asyncio
import os


api_id = 26102772
api_hash = '54a0b7d2b93fb51c50807d85e18ecd40'

# lst = [7478070952, 6388067367, 6903264582, 
#        6508314190, 6785254031, 6774119671, 
#        6807753588, 6496620987, 6788724315, 
#        6810623013, 6816260703, 6581321535]

lst = ['vladimir_might', 'anna_starlet', 'oleg_bolds', 
       'sveta_lightf', 'nikita_skyx', 'elena_bigger', 
       'victor_7777778', 'daria_sweetinger', 'igorstoperz', 
       'aleksey1235678', 'Alina_nemisi']
result = []
with TelegramClient('my', api_id, api_hash, system_version="4.10.5 beta x64") as client:
    users = client.iter_participants('Parsinger_Telethon_Test')
    for user in users:
        user_full_about = client(GetFullUserRequest(user))
        if user.username in lst:
            result.append(int(user_full_about.full_user.about))
print(sum(result))
