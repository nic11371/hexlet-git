import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# Инициализация драйвера
with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/7/7.3.4/index.html")
    element = browser.find_element(By.ID, "context-area")

    actions = ActionChains(browser)

    actions.context_click(element).perform()
    time.sleep(1)
    point = browser.find_element(By.CSS_SELECTOR, "div[data-action='get_password']")
    point.click()

    time.sleep(10)
