# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/5/index.html')
#     items = browser.find_elements(By.TAG_NAME, 'a')
#     expiries = []
#     for item in items:
#         url = item.get_attribute('href')
#         browser.get(url)
#         cookies = browser.get_cookies()
#         for cookie in cookies:
#             expiries.append(int(cookie.get('expiry')))
#         expiry_long = max(expiries)
#         for c in cookies:
#             if int(c['expiry']) == expiry_long:
#                 number = browser.find_element(By.ID, 'result')
#                 print(number.text)
#         browser.back()

#     time.sleep(10)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/5/index.html')
    links = browser.find_elements(By.TAG_NAME, 'a')

    max_expiry = 0
    result_number = 0

    for link in links:
        url = link.get_attribute('href')
        browser.get(url)

        # Получаем cookies текущей страницы
        cookies = browser.get_cookies()

        # Находим максимальный expiry среди всех cookies на странице
        current_max = max(int(cookie['expiry']) for cookie in cookies) if cookies else 0

        # Сравниваем с текущим максимальным
        if current_max > max_expiry:
            max_expiry = current_max
            result_number = int(browser.find_element(By.ID, 'result').text)

        # Возвращаемся на главную страницу
        browser.back()

    print(f"Найденное число: {result_number}")
    time.sleep(5)
