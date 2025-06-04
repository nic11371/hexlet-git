import requests


link = []

for num in range(1, 201):
    url = f'https://parsinger.ru/3.3/1/{num}.html'
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        # link.append(url)
        response_ok = requests.get(url, verify=False)
        response_ok.encoding = 'utf-8'
        link.append(response_ok.text)
        break

print(link)
