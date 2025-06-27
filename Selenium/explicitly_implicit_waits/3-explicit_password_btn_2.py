import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/4/index.html')
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    title = WebDriverWait(browser, 40).until(EC.title_contains("JK8HQ"))
    if title:
        print(browser.title)
    result = browser.find_element(By.ID, 'result').text
    print(result)
    time.sleep(3)
