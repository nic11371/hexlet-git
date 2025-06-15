import json
import requests
from bs4 import BeautifulSoup


url = 'https://parsinger.ru/html/index4_page_1.html'

response = requests.get(url=url, verify=False)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

result_json = []
pagen = int([link.text for link in soup.find('div', class_='pagen').find_all('a')][-1])
categories = int([link['href'][5:6] for link in soup.find('div', class_='nav_menu').find_all('a')][-1])
for category in range(1, categories + 1):
    for page in range(1, pagen + 1):

        url = f'https://parsinger.ru/html/index{category}_page_{page}.html'
        response = requests.get(url, verify=False)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        for card in soup.find_all('div', class_='item'):
            description = dict(map(str.strip, tag.text.split(':')) for tag in card.select('li'))
            price = card.find('p', class_='price').text.strip()

            result_json.append({"Наименование": card.find('a', class_='name_item').text.strip()} | description | {"Цена": price})
with open('../res2.json', 'w', encoding='utf-8-sig', newline='') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
