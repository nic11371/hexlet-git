import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.1.1/index.html')
    btns = browser.find_elements(By.TAG_NAME, "button")
    for btn in btns:
        WebDriverWait(browser, 15).until(EC.element_to_be_clickable(btn)).click()

    time.sleep(10)
