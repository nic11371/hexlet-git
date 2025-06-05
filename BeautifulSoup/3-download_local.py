import requests

# Указываем URL страницы
url = 'http://parsinger.ru/html/watch/1/1_1.html'

# Получаем HTML-код
response = requests.get(url)

# Сохраняем в файл
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(response.text)
print("Страница сохранена как index.html")