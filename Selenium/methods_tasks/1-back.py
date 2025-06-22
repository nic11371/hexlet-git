import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/6/6.2/index.html")
    browser.find_element(By.TAG_NAME, 'a').click()
    browser.find_element(By.TAG_NAME, 'a').click()
    browser.back()
    browser.back()

    time.sleep(20)