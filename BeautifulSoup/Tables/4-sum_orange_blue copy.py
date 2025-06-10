from bs4 import BeautifulSoup
import requests


url = 'https://parsinger.ru/table/5/index.html'
response = requests.get(url, verify=False)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

table = soup.find('table')

orange = table.find_all('td', class_='orange')
blue = soup.select('table tr td:nth-last-of-type(1)')
multiple = [float(o.text) * float(b.text) for o, b in zip(orange, blue)]

print(sum(multiple))