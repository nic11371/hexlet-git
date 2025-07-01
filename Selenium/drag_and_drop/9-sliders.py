import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://parsinger.ru/selenium/5.10/6/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    slider_containers = browser.find_elements(
        By.CLASS_NAME, "slider-container")

    for container in slider_containers:
        slider = container.find_element(By.CLASS_NAME, 'volume-slider')
        current_value = int(slider.get_attribute("value"))
        target_value = int(container.find_element(
            By.CLASS_NAME, "target-value").text)
        while current_value != target_value:
            if current_value < target_value:
                slider.send_keys(Keys.ARROW_RIGHT)
                current_value += 1
            else:
                slider.send_keys(Keys.ARROW_LEFT)
                current_value -= 1

    message_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "message"))
    )

    # Копируем сообщение
    message = message_element.text
    print("Сообщение:", message)
    time.sleep(10)
