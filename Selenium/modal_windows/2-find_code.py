import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/5.8/1/index.html")
    inputs = browser.find_elements(By.TAG_NAME, 'input')
    for i in inputs:
        i.click()
        time.sleep(.1)
        alert = browser.switch_to.alert
        alert.accept()
        result = browser.find_element(By.ID, 'result')
        if result.text:
            print(result.text)
    time.sleep(10)