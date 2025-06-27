import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html')
    while True:
        
        try:
            btn = browser.find_element(By.ID, "searchLink")
            btn.click()
            contain = WebDriverWait(browser, 5).until(EC.url_contains("qLChv49"))
            check = browser.find_element(By.ID, "checkButton")
            check.click()
            result = browser.find_element(By.ID, "password")
            print(result.text)
            break

        except Exception:
            browser.back()
    time.sleep(10)
