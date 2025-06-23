import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
    btns = browser.find_elements(By.CLASS_NAME, 'clickMe')
    total = []
    for btn in btns:
        browser.execute_script(
            "return arguments[0].scrollIntoView(true);", btn)
        btn.click()

    time.sleep(12)
