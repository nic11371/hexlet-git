from bs4 import BeautifulSoup
import requests


url = 'https://parsinger.ru/html/index3_page_1.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')


links_goods = []
articles = []
pagen = int([link.text for link in soup.find('div', class_='pagen').find_all('a')][-1])
for page in range(1, pagen + 1):
    url = f'https://parsinger.ru/html/index3_page_{page}.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    good = [g['href'] for g in soup.find_all('a', class_='name_item')]
    links_goods.append(good)


base_url = 'https://parsinger.ru/html/'
for links in links_goods:
    for link in links:
        url = f'{base_url}{link}'
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        article = soup.find('p', class_='article').text.replace('Артикул: ' ,'')
        articles.append(int(article))
print(sum(articles))
