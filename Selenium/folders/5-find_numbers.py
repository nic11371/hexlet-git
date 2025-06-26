from selenium import webdriver
from selenium.webdriver.common.by import By
import time


sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
        'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]

with webdriver.Chrome() as browser:
    total = []
    for site in sites:
        browser.switch_to.new_window('tab')
        browser.get(site)
        time.sleep(1)
    for x in range(len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[x])
        try:
            checkbox = browser.find_element(By.CLASS_NAME, 'checkbox_class')
            checkbox.click()
            result = browser.find_element(By.ID, 'result').text
            square = int(result) ** 0.5
            total.append(square)
        except Exception:
            pass

    summary = sum(total)
    print(round(summary, 9))

    time.sleep(10)
