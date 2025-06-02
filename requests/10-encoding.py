import requests

url = 'https://parsinger.ru/html/watch/1/1_2.html'
response = requests.get(url)
response.encoding = 'utf-8'
# Автоматически определённая кодировка (обычно берётся из заголовка Content-Type)
print("Текущая кодировка:", response.encoding)

# Посмотрим, как выглядит текст с текущей кодировкой
print("Пример текста с авто-определённой кодировкой:")
print(response.text)