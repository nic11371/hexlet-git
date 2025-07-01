import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


url = "https://parsinger.ru/selenium/5.10/8/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(0.5)
    browser.maximize_window()
    ranges = browser.find_elements(By.CLASS_NAME, 'range')
    pieces = browser.find_elements(By.CLASS_NAME, "piece")
    action = ActionChains(browser)

    for piece in pieces:
        box_color = piece.value_of_css_property("background-color")
        for range in ranges:
            square_color = range.value_of_css_property("background-color")
            if box_color == square_color:
                action.drag_and_drop(piece, range).perform()
                time.sleep(0.5)
                break

    time.sleep(10)
