from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('about:blank')
    browser.switch_to.new_window('tab')
    browser.get("https://parsinger.ru/selenium/8/8.1/site1/")
    title_1 = browser.title
    filter_num_1 = int("".join([i for i in title_1 if i not in {'4', '3', '9'}]))
    browser.switch_to.new_window("tab")
    browser.get("http://parsinger.ru/selenium/8/8.1/site2/")
    title_2 = browser.title
    filter_num_2 = int("".join([i for i in title_2 if i not in {'7', '8', '0'}]))
    print(filter_num_1 + filter_num_2)

    time.sleep(5)
