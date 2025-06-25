import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/5.8/2/index.html")
    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
    for b in buttons:
        b.click()
        time.sleep(.1)
        alert = browser.switch_to.alert
        num = alert.text
        alert.accept()
        field = browser.find_element(By.ID, 'input')
        field.send_keys(int(num))
        browser.find_element(By.ID, 'check').click()
        result = browser.find_element(By.ID, 'result').text
        if result != "Неверный пин-код":
            print(result)
            break
    time.sleep(10)
