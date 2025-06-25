import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/5.8/5/index.html")
    frames = browser.find_elements(By.TAG_NAME, "iframe")
    for f in frames:
        browser.switch_to.frame(f)
        btn = browser.find_element(By.TAG_NAME, "button")
        btn.click()
        display = browser.find_element(By.ID, 'numberDisplay')
        num = display.text
        browser.switch_to.default_content()
        field = browser.find_element(By.ID, 'guessInput')
        field.clear()
        field.send_keys(int(num))
        check = browser.find_element(By.ID, 'checkBtn')
        check.click()

    time.sleep(100)
