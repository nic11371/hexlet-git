import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/draganddrop/3/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    red_point = browser.find_element(By.ID, 'block1')
    action = ActionChains(browser)
    action.click_and_hold(red_point).perform
    points = browser.find_elements(By.CLASS_NAME, "controlPoint")

    for point in points:
        action.move_to_element(point)
    action.move_to_element(points[0])
    action.perform()

    time.sleep(10)
