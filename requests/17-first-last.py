import requests


pages = []

for num in range(1, 201):
    url = f'https://parsinger.ru/3.3/4/{num}.html'
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        pages.append(f'https://parsinger.ru/3.3/4/{num}.html')

first_available_page = pages[0]
last_available_page = pages[-1]

print(f"Первая доступная страница: {first_available_page}.html")
print(f"Последняя доступная страница: {last_available_page}.html")
