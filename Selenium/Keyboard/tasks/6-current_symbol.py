import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://parsinger.ru/selenium/5.6/3/index.html'


with webdriver.Chrome() as browser:

    browser.get(url=URL)

    for _ in range(364):

        letter = browser.find_element(By.CLASS_NAME, 'current-char').text

        if letter == '⎵':

            ActionChains(browser).send_keys(Keys.SPACE).perform()

        else:

            ActionChains(browser).send_keys(letter).perform()
        time.sleep(0.3)
    time.sleep(10)
