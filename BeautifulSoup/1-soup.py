import requests
from bs4 import BeautifulSoup

# Указываем URL страницы, которую хотим спарсить
url = 'http://parsinger.ru/html/watch/1/1_1.html'

# Отправляем GET-запрос и сохраняем ответ в переменную response
response = requests.get(url, verify=False)
response.encoding = 'utf-8'

# Создаем объект BeautifulSoup, передавая HTML-код и парсер
soup = BeautifulSoup(response.text, 'html.parser')

# Проверяем, что получилось
print(soup)

# Проверяем, тип объекта
print(type(soup))