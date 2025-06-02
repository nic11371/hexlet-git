import requests
import random # Не забываем импортировать random

url = 'http://httpbin.org/user-agent'

# --- Шаг 1: Чтение User-Agent'ов из файла ---
with open('user_agent.txt') as file:
    # Читаем все строки, убираем пустые строки и пробелы по краям
    user_agents_list = [line.strip() for line in file if line.strip()]


# --- Шаг 2: Выбор случайного User-Agent ---
random_user_agent = random.choice(user_agents_list)
print(f"Выбран случайный User-Agent: {random_user_agent}")

# --- Шаг 3: Формирование заголовков ---
headers = {'User-Agent': random_user_agent}

# --- Шаг 4: Выполнение запроса ---
response = requests.get(url=url, headers=headers)
response.raise_for_status() # Проверка на HTTP ошибки (4xx, 5xx)

print("Ответ сервера:")
print(response.text)
