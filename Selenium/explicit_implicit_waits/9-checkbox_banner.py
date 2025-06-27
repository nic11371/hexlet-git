import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/6/index.html')
    checkbox = WebDriverWait(browser, 30).until(EC.element_located_to_be_selected((By.ID, 'myCheckBox')))
    if checkbox:
        btn = browser.find_element(By.TAG_NAME, 'button')
        btn.click()
    result = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, 'result'))
        ).text
    print(result)
    time.sleep(10)
