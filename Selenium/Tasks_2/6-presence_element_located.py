import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.5.1/index.html')
    item = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.ID, 'order-number')))
    order = item.text
    print(order)
    time.sleep(10)
