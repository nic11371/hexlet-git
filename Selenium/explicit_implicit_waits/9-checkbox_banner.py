import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/6/index.html')
    checkbox = WebDriverWait(browser, 30).until(EC.element_located_to_be_selected((By.ID, 'myCheckBox')))
    button = WebDriverWait(browser, 10).until(
        lambda d: d.find_element(By.XPATH, "//button[text()='Проверить']") if d.find_element(
            By.ID, 'myCheckBox').is_selected() else False)
    button.click()
    result = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, 'result'))
        ).text
    print(result)
    time.sleep(10)
