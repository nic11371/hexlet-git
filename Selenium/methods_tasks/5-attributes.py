import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/5.5/2/1.html")
    fields = browser.find_elements(By.CSS_SELECTOR, 'input.text-field')
    for field in fields:
        attr = field.get_attribute("data-enabled")
        if attr:
            field.clear()
    browser.find_element(By.ID, 'checkButton').click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

    time.sleep(15)
