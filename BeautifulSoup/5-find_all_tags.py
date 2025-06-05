from bs4 import BeautifulSoup
import lxml


html ='''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Тестовая страница для веб-парсинга</title>
</head>
<body>
    <p id="435456" class="123984">Веб-парсинг – это мощный инструмент для анализа данных в интернете.</p>
    <p id="284359" class="493572">Python предоставляет отличные библиотеки для парсинга веб-страниц.</p>
    <p id="789234" class="293487">Для начинающих веб-парсеров важно изучить основы HTML и CSS.</p>
    <p id="239048" class="392874">Библиотека BeautifulSoup позволяет легко извлекать данные с веб-страниц.</p>
    <p id="923874" class="120948">Scrapy – другой популярный фреймворк для веб-парсинга на Python.</p>
    <p id="982374" class="302984">Веб-парсинг может помочь аналитикам и маркетологам собирать ценную информацию.</p>


</body>
</html>
'''


def sum_even_length_ids(html):
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('p')
    total_id = []
    total_class = []
    for tag in tags:
        text = tag.text
        if len(text.replace(" ", "")) % 2 == 0:
            tag_id = tag.get("id")
            total_id.append(int(tag_id))
            tag_class = tag.get("class")[0]
            total_class.append(int(tag_class))
    total_id_sum = sum(total_id)
    total_class_sum = sum(total_class)


    print(f"Сумма ID и CLASS тегов <p> с чётной длиной текста без пробелов: {total_id_sum + total_class_sum}")


sum_even_length_ids(html)