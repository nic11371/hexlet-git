import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/7/index.html')
    containers = browser.find_elements(By.CLASS_NAME, 'container')
    for container in containers:
        checkbox = container.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
        button = container.find_element(By.TAG_NAME, 'button')
        WebDriverWait(browser, 30).until(lambda d: checkbox.is_selected())
        button.click()
    result = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, 'result'))
        ).text
    print(result)
    time.sleep(10)
