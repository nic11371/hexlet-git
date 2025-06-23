import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.5/index.html')
    element = browser.find_element(By.ID, 'target')
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    element.click()
    time.sleep(12)
