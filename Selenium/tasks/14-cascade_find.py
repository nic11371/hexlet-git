import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.1/index.html')
    parent = browser.find_element(By.ID, "parent_id")
    child = parent.find_element(By.CLASS_NAME, 'child_class')
    child.click()
    password = child.get_attribute('password')
    print(password)

    time.sleep(10)
