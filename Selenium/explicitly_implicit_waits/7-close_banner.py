import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/4/index.html')
    close = browser.find_element(By.ID, 'closeBtn')
    WebDriverWait(browser, 6).until(EC.element_to_be_clickable(close)).click()
    ad = browser.find_element(By.ID, 'ad')
    WebDriverWait(browser, 10).until(EC.invisibility_of_element_located(ad))
    time.sleep(20)
