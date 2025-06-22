import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/methods/1/index.html")
    result = browser.find_element(By.ID, 'result').text
    digit_result = result.replace("Refresh Page", "")
    while True:
        browser.refresh()
        time.sleep(1)
        if digit_result:
            print(result)
            break

    time.sleep(20)
