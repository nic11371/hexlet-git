import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/2/index.html')
    locator = (By.ID, 'qQm9y1rk')
    element = WebDriverWait(browser, 50).until(
        EC.presence_of_element_located(locator)).click()
    time.sleep(10)
