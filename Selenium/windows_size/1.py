import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/8/8.2.1/index.html")
    browser.set_window_size(1200, 720)
    time.sleep(10)
