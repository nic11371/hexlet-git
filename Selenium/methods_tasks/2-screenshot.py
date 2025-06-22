import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/6/6.2.1/index.html")
    picture = browser.find_element(By.ID, 'this_pic')
    picture.screenshot("picture.png")

    time.sleep(5)