from bs4 import BeautifulSoup
import requests


url = 'https://parsinger.ru/table/1/index.html'
response = requests.get(url, verify=False)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

table = soup.find('table')
rows = table.find_all('tr')

total_rows = []

for row in rows[1:]:
    columns = row.find_all('td')
    for col in columns:
        if float(col.text) not in total_rows:
            total_rows.append(float(col.text))
            

print(sum(total_rows))