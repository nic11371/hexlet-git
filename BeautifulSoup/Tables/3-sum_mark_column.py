from bs4 import BeautifulSoup
import requests


url = 'https://parsinger.ru/table/4/index.html'
response = requests.get(url, verify=False)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

table = soup.find('table')

total_rows = []

mark_column = table.find_all('td', class_='green')

for i in mark_column:
    total_rows.append(float(i.text))

print(sum(total_rows))