import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

# Инициализация драйвера
with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/scroll/2/index.html")
    items = browser.find_elements(By.CLASS_NAME, "item")
    total = []
    for item in items:
        item.find_element(By.TAG_NAME, 'input').click()
        ActionChains(browser).move_to_element(item).scroll_by_amount(0, 50).perform()
        time.sleep(0.3)
        num = item.find_element(By.TAG_NAME, 'span').text
        if num != "":
            total.append(int(num))
    print(sum(total))
    time.sleep(10)
