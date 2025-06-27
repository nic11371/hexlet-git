import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.7.2/index.html')
    google = browser.find_element(By.CLASS_NAME, "search-box")
    google.send_keys("TEST")
    btn = browser.find_element(By.ID, 'search-button')
    btn.click()
    old = browser.find_element(By.ID, 'old-result')
    book = WebDriverWait(browser, 30).until(
        EC.staleness_of(old))
    WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Показать секрет']"))).click()
    result = browser.find_element(By.ID, 'result')
    print(result.text)
    time.sleep(20)
