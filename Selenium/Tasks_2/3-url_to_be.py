import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.3/index.html')
    btn = browser.find_element(By.CSS_SELECTOR, "a[href='final.html?loading=1']")
    btn.click()
    WebDriverWait(browser, 60).until(EC.url_to_be(
        "https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure"))
    result = browser.find_element(By.ID, "password")
    print(result.text)
    time.sleep(10)
