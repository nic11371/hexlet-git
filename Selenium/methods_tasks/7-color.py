import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/5.5/4/1.html")
    fields = browser.find_elements(By.CLASS_NAME, 'parent')
    for field in fields:
        gray = field.find_element(By.XPATH, ".//textarea[@color='gray']")
        blue = field.find_element(By.XPATH, ".//textarea[@color='blue']").send_keys(gray.text)
        gray.clear()
        btn = field.find_element(By.TAG_NAME, 'button')
        btn.click()

    time.sleep(30)
