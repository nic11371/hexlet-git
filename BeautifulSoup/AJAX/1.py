import requests

url = 'http://31.130.149.237/api/v1/ajax/GetSum'

params = {
    'GiveName': 'JPY',
    'GetName': 'DOGE',
    'Sum': 51284.43,
    'Direction': 1
}

response = requests.get(url=url, params=params)
answer = response.json()
print(answer.get('giveSum'))
