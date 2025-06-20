import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/4/4.html')
    checks = browser.find_elements(By.CLASS_NAME, "check")
    for check in checks:
        check.click()
    time.sleep(10)
