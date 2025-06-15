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

links_goods = []
for page in range(1, pagen + 1):
    url = f'https://parsinger.ru/html/index2_page_{page}.html'
    response = requests.get(url, verify=False)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    good = [g['href'] for g in soup.find_all('a', class_='name_item')]
    links_goods.append(good)

base_url = 'https://parsinger.ru/html/'

result_json = []

for links in links_goods:
    for link in links:
        url = f'{base_url}{link}'
        response = requests.get(url, verify=False)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        name = soup.find('p', id='p_header').text.strip()
        article = soup.find('p', class_='article').text.replace('Артикул: ', '').strip()
        count = soup.find('span', id='in_stock').text.strip().replace('В наличии: ', '')
        description = {tag['id']: tag.text.split(':')[1].strip() for tag in soup.select('li')}
        price = soup.find('span', id='price').text.strip()
        old_price = soup.find('span', id='old_price').text.strip()
        result_json.append(
            {"categories": "mobile"} |
            {"name": name} |
            {"article": article} |
            {"description": description} |
            {"count": count} |
            {"price": price} |
            {"old_price": old_price} |
            {"link": url}
        )

with open('../res3.json', 'w', encoding='utf-8-sig', newline='') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
