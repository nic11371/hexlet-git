import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

# Инициализация драйвера
with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/7/7.3.5/index.html")
    left = browser.find_element(By.ID, "scrollable-container-left")
    right = browser.find_element(By.ID, "scrollable-container-right")

    actions = ActionChains(browser)

    actions.click(left)
    for container in range(5):
        actions.key_down(Keys.END).perform()
        time.sleep(0.3)
        actions.key_up(Keys.END).perform()

    actions.click(right)
    for container in range(5):
        actions.key_down(Keys.END).perform()
        time.sleep(0.3)
        actions.key_up(Keys.END).perform()

    time.sleep(10)
