import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')
    btns = browser.find_elements(By.CLASS_NAME, 'box_button')
    total = []
    for btn in btns:
        btn.click()
        banner_locate = (By.ID, "ad_window")
        ad = WebDriverWait(browser, 100).until(EC.visibility_of_element_located(banner_locate))
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "close_ad"))).click()
        WebDriverWait(browser, 5).until(EC.invisibility_of_element_located(banner_locate))
        WebDriverWait(browser, 5).until(lambda _: btn.text != "")
        text = btn.text
        total.append(text)
    password = '-'.join(total)
    print(password)
    time.sleep(10)
