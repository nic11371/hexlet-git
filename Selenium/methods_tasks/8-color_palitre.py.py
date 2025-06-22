import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/5.5/5/1.html")
    container = browser.find_element(By.ID, 'main-container')
    blocks = container.find_elements(By.XPATH, './div')
    for d in blocks:
        span = d.find_element(By.TAG_NAME, 'span')
        options = d.find_elements(By.TAG_NAME, 'option')
        [opt.click() for opt in options if span.text == opt.text]
        btn_colors = d.find_elements(By.TAG_NAME, 'button')
        [btn.click() for btn in btn_colors if btn.get_attribute('data-hex') == span.text]
        checkbox = d.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        checkbox.click()
        field = d.find_element(By.CSS_SELECTOR, "input[type='text']")
        field.send_keys(span.text)
        btn = d.find_element(By.XPATH, ".//button[text()='Проверить']")
        btn.click()
    button = browser.find_element(By.XPATH, ".//button[text()='Проверить все элементы']")
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
