import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/selenium/5.7/4/index.html")
    total = []
    container = browser.find_element(By.ID, 'main_container')
    prev_count = 0
    while True:
        checks = browser.find_elements(By.TAG_NAME, 'input')
        for check in checks[len(total):]:
            total.append(check)
            value = check.get_attribute('value')
            if int(value) % 2 == 0:
                check.click()

        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", check)
        time.sleep(1)

        if len(total) == prev_count:
            break
        prev_count = len(total)
    time.sleep(10)
