from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/8/8.1.2/index.html")
    main = browser.current_window_handle
    input = browser.find_element(By.ID, 'sumInput')
    btn = browser.find_element(By.ID, 'checkButton')
    for p in range(1, 6):
        browser.switch_to.new_window("tab")
        browser.get(f"https://parsinger.ru/selenium/8/8.1.2/page{p}.html")
        time.sleep(3)

    numbers = []
    for x in range(len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[x])
        for y in browser.find_elements(By.CLASS_NAME, 'number'):
            num = y.text
            numbers.append(int(num))
        time.sleep(1)
    summary = sum(numbers)
    browser.switch_to.window(main)
    input.send_keys(summary)
    btn.click()
    time.sleep(50)
