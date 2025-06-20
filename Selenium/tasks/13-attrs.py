import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.3/index.html')
    links = browser.find_elements(By.TAG_NAME, "a")
    soldiers = []
    for link in links:
        attr = link.get_attribute("stormtrooper")
        if attr.isdigit():
            soldiers.append(int(attr))
    soldiers_sum = sum(soldiers)
    browser.find_element(By.ID, 'inputNumber').send_keys(soldiers_sum)
    browser.find_element(By.ID, 'checkBtn').click()

    time.sleep(10)
