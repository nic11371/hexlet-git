import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.2/index.html')
    cookie = browser.delete_all_cookies()

    time.sleep(10)
