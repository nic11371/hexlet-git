import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3/index.html')
    cookie = browser.get_cookies()
    song = cookie[0]['name']
    browser.find_element(By.ID, 'phraseInput').send_keys(song)
    browser.find_element(By.ID, 'checkButton').click()
    result = browser.find_element(By.ID, 'result').text
    print(result)

    time.sleep(10)
