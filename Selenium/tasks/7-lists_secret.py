import time
from selenium import webdriver
from selenium.webdriver.common.by import By

expression = ((12434107696 * 3) * 2) + 1
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    selectors = browser.find_elements(By.TAG_NAME, 'option')
    find_selector = [selector.click() for selector in selectors if expression == int(selector.text)]
    button = browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(10)
