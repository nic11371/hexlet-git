import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

# Инициализация драйвера
with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/7/7.3.3/index.html")
    instructions = browser.find_element(By.ID, "instructions")

    actions = ActionChains(browser)

    actions.key_down(Keys.CONTROL, instructions) \
        .key_down(Keys.ALT) \
        .key_down(Keys.SHIFT) \
        .key_down("T").perform()
    actions.key_up(Keys.CONTROL, instructions) \
        .key_up(Keys.ALT) \
        .key_up(Keys.SHIFT) \
        .key_up("T").perform()

    time.sleep(10)

