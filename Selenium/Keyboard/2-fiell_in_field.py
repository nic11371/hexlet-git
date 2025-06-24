import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get(r"https://parsinger.ru/selenium/7/7.2/index.html")

    list_input = []
    while len(list_input) <= 100:
        # Ищем все элементы input на веб-странице и добавляем их в список input_tags
        input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]

        # Обходим каждый элемент input в списке
        for tag_input in input_tags:
            # Проверяем, не обрабатывали ли мы уже этот элемент ранее
            if tag_input not in list_input:
                tag_input.send_keys("TEXT")
                tag_input.send_keys(Keys.ENTER)
                tag_input.send_keys(Keys.ARROW_DOWN)      
                time.sleep(.3)
                list_input.append(tag_input)

    result = browser.find_element(By.ID, 'hidden_password').text
    print(result)

