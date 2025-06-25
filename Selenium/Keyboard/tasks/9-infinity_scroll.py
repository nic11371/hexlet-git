import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

# Инициализация драйвера
with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/infiniti_scroll_1/")
    total = []
    container = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    # ActionChains(browser).move_to_element(container).scroll_by_amount(0, 50).perform()
    last = None
    while True:
        items = browser.find_elements(By.TAG_NAME, "span")
        for item in items[len(total):]:
            if item.text.isdigit():
                total.append(int(item.text))

        try:
            last_element = browser.find_element(By.CLASS_NAME, 'last-of-list')
            if last_element:
                break
        except:
            pass

        ActionChains(browser).move_to_element(container).scroll_by_amount(0, 500).perform()
        time.sleep(.5)
    print(sum(total))
    time.sleep(10)
