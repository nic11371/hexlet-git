import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.4/index.html')
    btn = browser.find_element(By.CSS_SELECTOR, "a[href='test.html?step=start']")
    btn.click()
    current_url = browser.current_url
    WebDriverWait(browser, 60).until(EC.url_changes(current_url))
    result = browser.find_element(By.ID, "password")
    print(result.text)
    time.sleep(10)
