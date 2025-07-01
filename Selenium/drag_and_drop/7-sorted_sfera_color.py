import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


url = "https://parsinger.ru/selenium/5.10/4/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(0.5)
    browser.maximize_window()
    squares = browser.find_elements(By.CLASS_NAME, 'basket_color')
    boxes = browser.find_elements(By.CLASS_NAME, "ball_color")
    action = ActionChains(browser)

    for box in boxes:
        box_color = box.value_of_css_property("background-color")
        for square in squares:
            square_color = square.value_of_css_property("background-color")
            if box_color == square_color:
                action.drag_and_drop(box, square).perform()
                time.sleep(0.5)
                break

    time.sleep(10)
