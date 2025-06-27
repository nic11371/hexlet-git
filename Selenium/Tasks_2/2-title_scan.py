import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.2.1/index.html')
    btn = browser.find_element(By.ID, "startScan")
    btn.click()
    WebDriverWait(browser, 30).until(EC.title_is("Access Granted"))
    result = browser.find_element(By.ID, 'passwordValue')
    print(result.text)
    time.sleep(10)
