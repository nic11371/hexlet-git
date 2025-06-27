import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.3/index.html')
    img = WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element_attribute(
            (By.ID, 'main_image'), "src", "success"))
    btn = browser.find_element(By.ID, 'main_image').click()
    btn.click()
    # result = WebDriverWait(browser, 30).until(
    #     EC.visibility_of_element_located((By.ID, 'password')))
    # print(result.text)
    time.sleep(10)
