import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.4/index.html')
    book_num = browser.find_element(By.ID, "booking-number").text
    input = browser.find_element(By.ID, "booking-input")
    book = WebDriverWait(browser, 30).until(
        EC.element_attribute_to_include(
            (By.ID, 'booking-number'), "confirmed"))
    input.send_keys(book_num)
    btn = browser.find_element(By.ID, 'check-button')
    btn.click()
    time.sleep(20)
