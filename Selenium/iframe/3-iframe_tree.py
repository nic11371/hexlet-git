import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/8/8.4.3/index.html")
    for _ in range(1, 4):
        frame = browser.find_element(By.TAG_NAME, "iframe")
        browser.switch_to.frame(frame)
        btn = browser.find_element(By.TAG_NAME, 'button')
        btn.click()

    time.sleep(100)
