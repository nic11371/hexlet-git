import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

url = "https://parsinger.ru/selenium/5.10/3/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    squares = browser.find_elements(By.CLASS_NAME, 'draganddrop_end')
    boxes = browser.find_elements(By.CLASS_NAME, "draganddrop")
    action = ActionChains(browser)
    # action.click_and_hold(red_point).perform

    for box in boxes:
        box_color = Color.from_string(
            box.value_of_css_property("background-color")).rgb
        box_hex = Color.from_string(box_color).hex
        for square in squares:
            square_color = Color.from_string(
                square.value_of_css_property("border-color")).rgb
            square_hex = Color.from_string(square_color).hex
            if box_hex == square_hex:
                action.click_and_hold(box).drag_and_drop(box, square).perform()
                time.sleep(0.5)
                break

    time.sleep(10)
