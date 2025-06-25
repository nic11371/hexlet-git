import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Инициализация драйвера
with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/5.7/5/index.html")
    buttons = browser.find_elements(By.TAG_NAME, "button")

    actions = ActionChains(browser)
    for btn in buttons:
        delay = float(btn.text)
        actions.click_and_hold(btn).pause(delay).release(btn).perform()

    time.sleep(10)
