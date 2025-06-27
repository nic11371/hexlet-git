import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.implicitly_wait(60)
    browser.get('https://parsinger.ru/selenium/9/9.3.1/index.html')
    btn = browser.find_element(By.ID, "startButton")
    btn.click()
    for _ in range(5):
        dynamic_btn = browser.find_element(By.ID, 'dynamicButton')
        dynamic_btn.click()
    result = browser.find_element(By.ID, 'secretPassword')
    print(result.text)
    time.sleep(10)
