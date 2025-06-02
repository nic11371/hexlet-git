import requests

# URL для примеров
url = "https://parsinger.ru/selenium/6/6.3.1/index.html"

# Выполняем GET-запрос
response = requests.get(url)

print(response.status_code)
print(response.text)
print(response.headers)
print(response.cookies)