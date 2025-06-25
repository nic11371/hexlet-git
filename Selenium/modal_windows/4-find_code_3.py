import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/5.8/3/index.html")
    buttons = browser.find_elements(By.CLASS_NAME, 'pin')
    for b in buttons:
        pin = b.text
        browser.find_element(By.ID, 'check').click()
        time.sleep(1)
        alert = browser.switch_to.alert
        alert.send_keys(pin)
        alert.accept()
        time.sleep(.5)
        result = browser.find_element(By.ID, 'result').text
        if result != "Неверный пин-код":
            print(result)
            break
    time.sleep(10)
