import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

# Инициализация драйвера
with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/7/7.4.1/index.html")
    body = browser.find_element(By.CLASS_NAME, "long-page")
    ActionChains(browser).move_to_element(body).scroll_by_amount(0, 1000).perform()
    time.sleep(4)
    password = browser.find_element(By.CLASS_NAME, 'countdown').text[5:]
    ActionChains(browser).move_to_element(body).scroll_by_amount(0, 1000).perform()
    input = browser.find_element(By.TAG_NAME, 'input').send_keys(password)
    btn = browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(2)
    time.sleep(10)