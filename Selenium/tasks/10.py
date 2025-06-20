import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
    browser.find_element(By.TAG_NAME, "input").send_keys('Дрогон')
    browser.find_element(By.ID, 'clickButton').click()
    time.sleep(10)
