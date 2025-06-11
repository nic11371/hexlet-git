import csv
import requests
from bs4 import BeautifulSoup


url = 'https://parsinger.ru/html/index4_page_1.html'

response = requests.get(url=url, verify=False)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

pagen = int([link.text for link in soup.find('div', class_='pagen').find_all('a')][-1])
categories = int([link['href'][5:6] for link in soup.find('div', class_='nav_menu').find_all('a')][-1])
for category in range(1, categories + 1):
    for page in range(1, pagen + 1):

        url = f'https://parsinger.ru/html/index{category}_page_{page}.html'
        response = requests.get(url, verify=False)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        name = [g.text.strip() for g in soup.find_all('a', class_='name_item')]
        description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
        price = [x.text.strip() for x in soup.find_all('p', class_='price')]
        with open('BeautifulSoup/CSV/res3.csv', 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for item, descr, price in zip(name, description, price):

                flatten = item, *[x.split(':')[1].strip() for x in descr if x], price
                writer.writerow(flatten)
