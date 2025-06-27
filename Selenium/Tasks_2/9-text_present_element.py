import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.1/index.html')
    items = WebDriverWait(browser, 130).until(
        EC.text_to_be_present_in_element((By.ID, 'usd-rate'), "75.50 ₽"))
    result = WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.ID, 'secret-code')))
    print(result.text)
    time.sleep(10)
