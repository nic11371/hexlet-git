import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_forms = browser.find_elements(By.CLASS_NAME, 'form')
    for form in input_forms:
        form.send_keys('Text')
    browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(10)
