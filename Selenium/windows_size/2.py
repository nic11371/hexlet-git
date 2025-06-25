import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/8/8.2.2/index.html")
    height = browser.get_window_size().get('height')
    width = browser.get_window_size().get('width')
    result = int(height) + int(width)
    print(result)
    time.sleep(10)
