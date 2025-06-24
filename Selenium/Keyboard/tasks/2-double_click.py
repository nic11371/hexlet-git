import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Инициализация драйвера
with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/7/7.3.2/index.html")
    dbclick = browser.find_element(By.ID, "dblclick-area")

    actions = ActionChains(browser)

    actions.double_click(dbclick).perform()

    time.sleep(10)

