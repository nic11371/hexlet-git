import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

# Инициализация драйвера
with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/infiniti_scroll_2/")
    total = []
    container = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    prev_count = 0
    while True:
        items = browser.find_elements(By.TAG_NAME, "p")
        for item in items[len(total):]:
            if item.text.isdigit():
                total.append(int(item.text))

        ActionChains(browser).move_to_element(container).scroll_by_amount(0, 500).perform()
        time.sleep(.5)

        if len(total) == prev_count:
            break
        prev_count = len(total)
    print(sum(total))
    time.sleep(10)
