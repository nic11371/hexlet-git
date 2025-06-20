import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
    btn = browser.find_element(By.ID, "secret-key-button")
    btn.click()
    secret = btn.get_attribute("data")
    print(secret)
    time.sleep(10)
