import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/5.5/3/1.html")
    fields = browser.find_elements(By.CLASS_NAME, 'parent')
    total = []
    for field in fields:
        checkbox = field.find_element(By.CSS_SELECTOR, 'input.checkbox')
        textarea = field.find_element(By.TAG_NAME, 'textarea').text
        if checkbox.is_selected():
            total.append(int(textarea))
    print(sum(total))

    time.sleep(15)
