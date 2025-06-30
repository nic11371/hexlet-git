import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/draganddrop/1/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)

    # Находим элементы
    draganddrop = browser.find_element(By.ID, "field1")
    draganddrop_end = browser.find_element(By.ID, "field2")

    # Выполняем перетаскивание
    ActionChains(browser).drag_and_drop(draganddrop, draganddrop_end).perform()
    time.sleep(5)
