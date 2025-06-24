import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Инициализация драйвера
with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/7/7.3.1/index.html")
    draggable = browser.find_element(By.ID, "draggable")
    target = browser.find_element(By.ID, "target")

    actions = ActionChains(browser)

    actions.drag_and_drop(draggable, target).perform()

    time.sleep(10)

