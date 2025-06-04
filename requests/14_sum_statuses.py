import requests

url_start = 'https://parsinger.ru/3.3/2/1.html'
url_stop = 'https://parsinger.ru/3.3/2/200.html'

statuses = []

for num in range(1, 201):
    url = f'https://parsinger.ru/3.3/2/{num}.html'
    response = requests.get(url, verify=False)
    statuses.append(response.status_code)

print(sum(statuses))
