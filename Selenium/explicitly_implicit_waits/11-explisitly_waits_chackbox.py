from selenium.common.exceptions import TimeoutException
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/7/index.html')

    # Создание словаря: {checkbox_element: его контейнер (div)}
    dct = {container.find_element(
        By.TAG_NAME, 'input'): container for container in browser.find_elements(
            By.CLASS_NAME, 'container')}

    # Проверка и ожидание пока словарь не пуст
    while dct:
        try:
            # Ожидание списка чекбоксов с .is_selected
            selected_inputs = WebDriverWait(browser, 20).until(
                lambda driver: [checkbox for checkbox in dct if checkbox.is_selected()] or None)

            for inp in selected_inputs:
                # Клик по кнопке в соответствующем контейнере
                dct[inp].find_element(By.TAG_NAME, 'button').click()
                # Удаление обработанного чекбокса из процесса проверки
                del dct[inp]

        except TimeoutException:
            pass

    print(WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p#result'))).text)
