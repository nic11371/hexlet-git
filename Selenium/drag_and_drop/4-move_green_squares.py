import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.10/2/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    # container = browser.find_element(By.ID, 'main_container')
    draganddrop_end = browser.find_element(By.CLASS_NAME, "draganddrop_end")
    action = ActionChains(browser)
    for n in range(1, 11):
        point = browser.find_element(By.ID, f"draganddrop{n}")

        action.drag_and_drop(point, draganddrop_end).perform()

    time.sleep(10)
