import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.7.1/index.html')
    address = browser.find_element(By.ID, 'address')
    address.send_keys("Moscow")
    payments = browser.find_element(By.XPATH, "//option[@value='card']").click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            ((By.ID, 'submit-order')))).click()
    WebDriverWait(browser, 20).until(
        EC.invisibility_of_element_located((By.ID, 'spinner'))
    )
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            ((By.ID, 'confirm-address')))).click()
    WebDriverWait(browser, 20).until(
        EC.invisibility_of_element_located((By.ID, 'modal'))
    )
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            ((By.ID, 'get-code')))).click()
    result = browser.find_element(By.ID, 'result')
    print(result.text)
    time.sleep(20)
