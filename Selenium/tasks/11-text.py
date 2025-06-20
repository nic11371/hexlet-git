import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
    browser.find_element(By.ID, "showTextBtn").click()
    password = browser.find_element(By.ID, 'text1').text
    browser.find_element(By.ID, "userInput").send_keys(password)
    browser.find_element(By.ID, "checkBtn").click()
    final_key = browser.find_element(By.ID, "text2").text
    print(final_key)
    time.sleep(10)
