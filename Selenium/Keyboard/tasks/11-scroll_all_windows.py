import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def window_scroll(browser, window_element):
    total = []
    container = window_element.find_element(By.CSS_SELECTOR, "div[class^='scroll-container']")
    prev_count = 0
    while True:
        browser.execute_script("arguments[0].scrollBy(0, arguments[0].scrollHeight);", container)
        time.sleep(.5)

        items = window_element.find_elements(By.TAG_NAME, "span")
        for item in items[len(total):]:
            if item.text.isdigit():
                total.append(int(item.text))

        if len(total) == prev_count:
            break
        prev_count = len(total)
    return sum(total)


with webdriver.Chrome() as browser:

    browser.get("https://parsinger.ru/infiniti_scroll_3/")

    total = []
    for n in range(6):
        windows = browser.find_elements(By.XPATH, f"//div[@id='scroll-wrapper_{n}']")
        for window in windows:
            sum_numbers = window_scroll(browser, window)
            total.append(sum_numbers)
    print(sum(total))
    time.sleep(5)
