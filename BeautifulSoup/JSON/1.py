import json
import requests
from bs4 import BeautifulSoup


url = 'https://parsinger.ru/html/index4_page_1.html'

response = requests.get(url=url, verify=False)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

result_json = []
pagen = int([link.text for link in soup.find('div', class_='pagen').find_all('a')][-1])
for page in range(1, pagen + 1):

    url = f'https://parsinger.ru/html/index4_page_{page}.html'
    response = requests.get(url, verify=False)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    for card in soup.find_all('div', class_='img_box'):
        description = card.find('div', class_='description')
        description_items = [d.text.strip() for d in description.find_all('li')]
        data = {
            "Наименование": card.find('a', class_='name_item').text.strip(),
            "Бренд": description_items[0].split(':')[1].strip(),
            "Форм-фактор": description_items[1].split(':')[1].strip(),
            "Ёмкость": description_items[2].split(':')[1].strip(),
            "Объем буферной памяти": description_items[3].split(':')[1].strip(),
            "Цена": card.find('p', class_='price').text.strip()
        }

        result_json.append(data)
with open('../res.json', 'w', encoding='utf-8-sig', newline='') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
