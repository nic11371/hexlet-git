from bs4 import BeautifulSoup
import requests
import json

result_list = list()

# ща мы сделаем так, чтобы код не зависил от кол-ва электроники, хоть 32, хоть 132
rq = requests.get(url='https://parsinger.ru/html/index2_page_1.html') # идем на 1 страницу товара
syp = BeautifulSoup(rq.text, 'lxml') # суп
last_link = syp.find('div', class_='pagen').find_all('a')[-1]['href'] # тут мы узнали последнюю страницу товара - index3_page_4.html
rq = requests.get(url='https://parsinger.ru/html/' + last_link) # идем на эту страницу
syp = BeautifulSoup(rq.text, 'lxml') # суп
amount = int(syp.find_all('a', class_='name_item')[-1]['href'].rstrip('.html').split('_')[1])
# помянем ваши глаза, но тут мы нашли число 32(кол-во товара) mouse/3/3_32.html => mouse/3/3_32 => ['mouse/3/3', '32'] => int(32)

for page in range(1, amount + 1):
    link = f'https://parsinger.ru/html/mobile/2/2_{page}.html' # формируем ссылку
    req = requests.get(url=link)
    req.encoding = 'utf-8'
    soup = BeautifulSoup(req.text, 'lxml')
    saver = dict() # тут собираем данные с каждой мышки
    saver['categories'] = 'mobile' # категория
    name = soup.find('p', id='p_header').text # имя
    article = soup.find('p', class_='article').text.split(':')[1].strip() # артикул
    description = {i['id']:i.text.split(':')[1].strip() for i in soup.find_all('li')} # собираем бренд и тд.
    count = soup.find('span', id='in_stock').text.split(':')[1].strip() # кол-во
    price = soup.find('span', id='price').text # цена
    old_price = soup.find('span', id='old_price').text # старая цена
    # теперь всё добавляем
    saver['name'] = name
    saver['article'] = article
    saver['description'] = description
    saver['count'] = count
    saver['price'] = price
    saver['old_price'] = old_price
    saver['link'] = link
    result_list.append(saver)

with open('mouses.json', 'w', encoding='utf-8') as file:
    json.dump(result_list, file, indent=4, ensure_ascii=False) # я еще на стадии изучения понял, что лучше сразу найти кол-во товара, а не писать 32, ведь надо быть готовым ко всему