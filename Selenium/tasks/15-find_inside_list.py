import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.2/index.html')
    blocks = browser.find_elements(By.CLASS_NAME, "block")
    for block in blocks:
        block.find_element(By.CLASS_NAME, "button").click()

    password = browser.find_element(By.TAG_NAME, "password").text
    print(password)

    time.sleep(10)
