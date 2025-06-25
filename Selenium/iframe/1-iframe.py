import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/8/8.4.1/")
    iframe = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(iframe)
    text = browser.find_element(By.TAG_NAME, 'body')
    words = text.text.split('*')
    result = []
    for i, w in enumerate(words):
        if i % 2 != 0:
            result.append(w)
    print("".join(result))
    time.sleep(10)
