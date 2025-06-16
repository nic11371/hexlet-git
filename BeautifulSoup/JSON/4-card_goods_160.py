from bs4 import BeautifulSoup
import requests
import json

base_url = 'https://parsinger.ru/html/'
result_list = []

# 1. Получаем все категории
main_page = requests.get(base_url + 'index1_page_1.html')
main_soup = BeautifulSoup(main_page.text, 'lxml')
category_links = [a for a in main_soup.select('.nav_menu a')]

for link in category_links:
    category_link = link['href']
    category = link.find('div')['id']  # например 'mobile'
    first_page_url = base_url + category_link

    # 2. Узнаем количество страниц в категории
    cat_resp = requests.get(first_page_url)
    cat_resp.encoding = 'utf-8'
    cat_soup = BeautifulSoup(cat_resp.text, 'lxml')
    pagen_links = cat_soup.select('.pagen a')
    total_pages = int(pagen_links[-1].text) if pagen_links else 1

    for page in range(1, total_pages + 1):
        page_url = f'{base_url}{category_link}'
        page_resp = requests.get(page_url)
        page_soup = BeautifulSoup(page_resp.text, 'lxml')

        product_links = [base_url + a['href'] for a in page_soup.select('.name_item')]

        for product_url in product_links:
            prod_resp = requests.get(product_url)
            prod_resp.encoding = 'utf-8'
            prod_soup = BeautifulSoup(prod_resp.text, 'lxml')

            # 3. Сбор данных
            item = {
                'categories': category,
                'name': prod_soup.find('p', id='p_header').text.strip(),
                'article': prod_soup.find('p', class_='article').text.split(':')[1].strip(),
                'description': {
                    li['id']: li.text.split(':')[1].strip()
                    for li in prod_soup.find_all('li')
                },
                'count': prod_soup.find('span', id='in_stock').text.split(':')[1].strip(),
                'price': prod_soup.find('span', id='price').text.strip(),
                'old_price': prod_soup.find('span', id='old_price').text.strip(),
                'link': product_url
            }

            result_list.append(item)

# 4. Сохраняем
with open('res4.json', 'w', encoding='utf-8') as file:
    json.dump(result_list, file, indent=4, ensure_ascii=False)
