from bs4 import BeautifulSoup
import requests


url = 'https://parsinger.ru/html/index3_page_1.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')


links_goods = []
total = []
pagen = int([link.text for link in soup.find('div', class_='pagen').find_all('a')][-1])
categories = int([link['href'][5:6] for link in soup.find('div', class_='nav_menu').find_all('a')][-1])
for category in range(1, categories + 1):
    for page in range(1, pagen + 1):
        url = f'https://parsinger.ru/html/index{category}_page_{page}.html'
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        good = [g['href'] for g in soup.find_all('a', class_='name_item')]
        links_goods.append(good)

print(links_goods)

base_url = 'https://parsinger.ru/html/'
for links in links_goods:
    for link in links:
        url = f'{base_url}{link}'
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        price = soup.find('span', id='price').text.replace(' руб','')
        amount = soup.find('span', id='in_stock').text.replace('В наличии: ' ,'')
        total_sum = float(price) * int(amount)
        total.append(total_sum)
print(sum(total))
