from bs4 import BeautifulSoup
import requests


url = 'https://parsinger.ru/table/5/index.html'
response = requests.get(url, verify=False)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

table = soup.find('table')
dictionary = {}

headers = table.find_all('th')
for i, n in enumerate(headers):
    header = n.text
    column_tags = table.select(f'tr td:nth-of-type({i + 1})')
    column = [float(t.text) for t in column_tags]
    dictionary[header] = round(sum(column), 3)

print(dictionary)
