import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/8/8.4.2/index.html")
    for n in range(1, 4):
        frame = browser.find_element(By.XPATH, f"//iframe[@id='frame{n}']")
        browser.switch_to.frame(frame)
        btn = browser.find_element(By.TAG_NAME, 'button')
        btn.click()
        browser.switch_to.default_content()

    time.sleep(10)
