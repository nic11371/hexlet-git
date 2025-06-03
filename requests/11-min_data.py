import requests

r = requests.get('https://parsinger.ru/3.4/1/json_weather.json', verify=False)

print(min(r.json(), key=lambda x: int(x['Температура воздуха'].strip('°C')))['Дата'])
