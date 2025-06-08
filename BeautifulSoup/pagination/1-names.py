from bs4 import BeautifulSoup
import requests


url = 'https://parsinger.ru/html/index3_page_1.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')


goods = []
pagen = int([link.text for link in soup.find('div', class_='pagen').find_all('a')][-1])
for page in range(1, pagen + 1):
    url = f'https://parsinger.ru/html/index3_page_{page}.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    good = [g.text for g in soup.find_all('a', class_='name_item')]
    goods.append(good)

print(goods)
