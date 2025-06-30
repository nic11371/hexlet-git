import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/draganddrop/2/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    red_point = browser.find_element(By.ID, 'draggable')
    points = browser.find_elements(By.CLASS_NAME, "box")
    action = ActionChains(browser)
    # action.click_and_hold(red_point).perform

    for point in points:
        action.drag_and_drop(red_point, point).perform()

    result = browser.find_element(By.ID, 'message')
    print(result)
    time.sleep(10)
