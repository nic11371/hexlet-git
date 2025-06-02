import requests

base_url = 'https://httpbin.org/get'

# Параметры, которые мы хотим передать
payload = {
    'query': 'web scraping',
    'language': 'python',
    'pages': 5
}

response = requests.get(base_url, params=payload)
response.raise_for_status() # Проверяем на HTTP ошибки

# 1. Посмотрим на сформированный URL
print(f"Итоговый URL: {response.url}\n")

# 2. Посмотрим, как сервер "увидел" наши параметры (в поле 'args')
data = response.json() # Ответ от httpbin - это JSON
print("Параметры, полученные сервером (args):")
print(data.get('args'))