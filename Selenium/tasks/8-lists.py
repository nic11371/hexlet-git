import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')
    checks = browser.find_elements(By.TAG_NAME, "option")
    total_checks = [int(check.text) for check in checks]
    print(sum(total_checks))
    time.sleep(10)
