import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    total_sum = []
    for cookie in cookies:
        digit = cookie['name'].split('_')
        number = int(digit[2])
        if number % 2 == 0:
            value = cookie['value']
            total_sum.append(int(value))
    print(sum(total_sum))
    time.sleep(10)
