import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


url = "https://parsinger.ru/draganddrop/4/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    word = browser.find_element(By.ID, "target-word").text
    alphabet = browser.find_elements(By.CLASS_NAME, "draggable-letter")
    slots = browser.find_elements(By.CLASS_NAME, 'letter-slot')
    action = ActionChains(browser)
    for i, w in enumerate(word):
        for a in alphabet:
            if a.text == w:
                action.drag_and_drop(a, slots[i]).perform()
                break

    message_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )

    # Копируем сообщение
    message = message_element.text
    print("Сообщение:", message)
    time.sleep(10)
