from bs4 import BeautifulSoup
import requests


url = 'https://parsinger.ru/table/1/index.html'
response = requests.get(url, verify=False)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

table = soup.find('table')
rows = table.find_all('tr')

total_rows = []

first_column = soup.select('table tr td:nth-of-type(1)')

for i in first_column:
    total_rows.append(float(i.text))

print(sum(total_rows))