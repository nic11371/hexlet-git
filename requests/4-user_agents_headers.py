import requests


url = 'http://31.130.149.237/user_agent'

headers = {
    'User-Agent': 'BaIII User-agent 007',
    'Accept': 'All what you give',
    'Accept-Language': 'Dothraki, Sindarin',
    'Accept-Encoding': 'br, gzip, dzen, sarcasm',
    'Referer': 'where_did_you_come_from.com',
    'DFSHDRFAEHERHRAEH': 'where_did_you_come_from.com',
}

response = requests.get(url=url, headers=headers)

print("Ответ сервера:")
print(response.text)
