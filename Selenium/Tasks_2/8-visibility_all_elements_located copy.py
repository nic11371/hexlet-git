import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.5.3/index.html')
    load = browser.find_element(By.ID, 'showProducts')
    load.click()
    items = WebDriverWait(browser, 30).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, 'product')))
    prices = []
    for item in items:
        price = item.find_element(By.CLASS_NAME, 'price')
        price_num = price.text
        prices.append(int(price_num[1:]))
    summary_price = sum(prices)
    input = browser.find_element(By.ID, 'sumInput')
    input.send_keys(summary_price)
    check = browser.find_element(By.ID, 'checkSum')
    check.click()
    result = WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.ID, 'secretMessage')))
    print(result.text)
    time.sleep(10)
