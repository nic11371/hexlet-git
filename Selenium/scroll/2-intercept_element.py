import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/scroll/4/index.html')
    btns = browser.find_elements(By.CLASS_NAME, 'btn')
    total = []
    for btn in btns:
        browser.execute_script(
            "return arguments[0].scrollIntoView(true);", btn)
        btn.click()
        time.sleep(1)
        result = browser.find_element(By.ID, 'result').text
        total.append(int(result))
    print(sum(total))

    time.sleep(12)
