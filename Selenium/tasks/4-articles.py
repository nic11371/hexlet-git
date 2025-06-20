import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    tags = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    total_tag = [int(tag.text) for tag in tags]
    time.sleep(10)
    print(sum(total_tag))
