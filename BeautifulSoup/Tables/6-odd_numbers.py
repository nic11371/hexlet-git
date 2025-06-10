from bs4 import BeautifulSoup
import requests


url = 'https://parsinger.ru/table/7/index.html'
response = requests.get(url, verify=False)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

tables = soup.find_all('table')
total_sum_tree = []

for table in tables:
    td = table.find_all('td')
    for n in td:
        num = int(n.text)
        if num % 3 == 0:
            total_sum_tree.append(num)


print(sum(total_sum_tree))
