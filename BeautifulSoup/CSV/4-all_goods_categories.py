import csv
import requests
from bs4 import BeautifulSoup


url = 'https://parsinger.ru/html/index1_page_1.html'

response = requests.get(url=url, verify=False)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

headers = [ 'Наименование', 'Артикул', 'Бренд', 'Модель',
    'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром']


links_goods = []
with open('BeautifulSoup/CSV/res4.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(headers)

pagen = int([link.text for link in soup.find('div', class_='pagen').find_all('a')][-1])
categories = int([link['href'][5:6] for link in soup.find('div', class_='nav_menu').find_all('a')][-1])
for category in range(1, categories + 1):
    for page in range(1, pagen + 1):

        url = f'https://parsinger.ru/html/index1_page_{page}.html'
        response = requests.get(url, verify=False)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        good = [g['href'] for g in soup.find_all('a', class_='name_item')]
        links_goods.append(good)

base_url = 'https://parsinger.ru/html/'
for links in links_goods:
    for link in links:
        url = f'{base_url}{link}'
        response = requests.get(url, verify=False)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        name = [g.text.strip() for g in soup.find_all('p', id='p_header')]
        article = [art.text.replace('Артикул: ' ,'').strip() for art in soup.find_all('p', class_='article')]
        description = [x.text.strip().split('\n') for x in soup.find_all('ul', id='description')]

        amount = [a.text.replace("В наличии: ", "").strip() for a in soup.find_all('span', id='in_stock')]
        new_price = [x.text.strip() for x in soup.find_all('span', id='price')]
        old_price = [x.text.strip() for x in soup.find_all('span', id='old_price')]
        with open('BeautifulSoup/CSV/res4.csv', 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for item, art, descr, am, new_price, old_price in zip(name, article, description, amount, new_price, old_price):
                filtered_descr = [x.split(':')[1].strip() for x in descr if x.startswith('Бренд:') or x.startswith('Модель:')]
                flatten = item, art, *filtered_descr, am, new_price, old_price, url
                writer.writerow(flatten)
