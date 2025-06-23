import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.3/index.html')
    cookie = {'name': 'secretKey', 'value': 'selenium123'}
    browser.add_cookie(cookie)
    browser.refresh()
    password = browser.find_element(By.ID, 'password').text
    print(password)
    time.sleep(10)
