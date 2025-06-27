import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.7.3/index.html')
    btn_page = browser.find_element(By.ID, 'summonBtn')
    btn_page.click()
    WebDriverWait(browser, 30).until(
        EC.number_of_windows_to_be(5))
    btn_pass = browser.find_element(By.ID, 'passwordBtn')
    btn_pass.click()
    alert = WebDriverWait(browser, 20).until(
        EC.alert_is_present()
    )
    result = alert.text
    print(result)
    time.sleep(20)
