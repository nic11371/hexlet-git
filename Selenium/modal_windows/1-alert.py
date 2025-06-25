import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/8/8.3.1/index.html")
    alert_btn = browser.find_element(By.ID, 'alertButton').click()
    time.sleep(1)
    alert = browser.switch_to.alert
    alert.accept()
    prompt_btn = browser.find_element(By.ID, 'promptButton').click()
    time.sleep(1)
    prompt = browser.switch_to.alert
    prompt.send_keys("Alert")
    prompt.accept()
    confirm_btn = browser.find_element(By.ID, 'confirmButton').click()
    time.sleep(1)
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(10)