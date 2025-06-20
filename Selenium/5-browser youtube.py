from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from undetected_chromedriver import Chrome, ChromeOptions
import random
import time
import os

# 1. Настройка stealth-браузера
def setup_browser():
    options = ChromeOptions()
    
    # Настройки прокси (рекомендуется резидентный мобильный прокси)
    proxy_options = {
        "proxy": {
            "http": f"http://jNstZ3:UUfzwg@95.181.172.108:8000",
            "https": f"http://jNstZ3:UUfzwg@95.181.172.108:8000"
        }
    }
    
    # Конфигурация Chrome
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument(f"--user-data-dir={os.path.expanduser('~')}/chrome_yt_profile")
    
    # Инициализация undetected-chromedriver
    driver = Chrome(options=options, seleniumwire_options=proxy_options)
    return driver

# 2. Человекообразные действия
def human_interaction(driver):
    actions = [
        lambda: driver.execute_script("window.scrollBy(0, 200)"),
        lambda: time.sleep(random.uniform(0.5, 2.0)),
        lambda: driver.find_element(By.TAG_NAME, "body").click()
    ]
    random.shuffle(actions)
    [action() for action in actions]

try:
    # 3. Многоэтапная авторизация
    driver = setup_browser()
    
    # Этап 1: Предварительный вход через нейтральный сайт
    driver.get("https://www.google.com/search?q=weather")
    human_interaction(driver)
    time.sleep(3)
    
    # Этап 2: Очистка куков Google
    driver.delete_all_cookies()
    
    # Этап 3: Ручная авторизация (критически важно)
    driver.get("https://accounts.google.com")
    input(">>> Войдите ВРУЧНУЮ в аккаунт Google, затем нажмите Enter...")
    
    # Этап 4: Ожидание и проверка
    WebDriverWait(driver, 15).until(
        EC.url_contains("myaccount.google.com")
    )
    print("Авторизация успешна!")
    
    # Этап 5: Доступ к YouTube
    driver.get("https://youtube.com")
    time.sleep(5)
    print("YouTube загружен!")
    
    # Бесконечное ожидание
    input("Нажмите Enter для выхода...")

finally:
    driver.quit()