import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 1. Сначала работаем в видимом режиме для расчета поправок
chrome_options = Options()
# chrome_options.add_argument('--headless')  # Пока отключаем для расчета дельт

# Исходные размеры из задания
base_sizes_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
base_sizes_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome(options=chrome_options) as browser:
    # 2. Расчет дельт в видимом режиме
    browser.get("https://parsinger.ru/window_size/2/index.html")
    time.sleep(2)
    
    # Устанавливаем тестовый размер
    test_x, test_y = 800, 600
    browser.set_window_size(test_x, test_y)
    time.sleep(1)
    
    # Получаем реальные размеры через JavaScript
    actual_width = browser.execute_script("return window.innerWidth")
    actual_height = browser.execute_script("return window.innerHeight")
    
    # Рассчитываем дельты
    delta_x = test_x - actual_width
    delta_y = test_y - actual_height
    print(f"Рассчитанные поправки: delta_x={delta_x}, delta_y={delta_y}")
    
    # 3. Применяем поправки к базовым размерам
    adjusted_sizes_x = [x + delta_x for x in base_sizes_x]
    adjusted_sizes_y = [y + delta_y for y in base_sizes_y]
    
    # 4. Теперь запускаем в headless режиме с поправками
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1000,1000')  # Устанавливаем большую высоту
    
    found = False
    result_code = ""
    
    # 5. Перебираем все сочетания с поправками
    for x in adjusted_sizes_x:
        for y in adjusted_sizes_y:
            browser.set_window_size(x, y)
            time.sleep(0.3)  # Даем время на применение размера
            
            result = browser.find_element(By.ID, 'result').text
            if result:
                # Вычисляем исходные размеры без поправок
                original_x = x - delta_x
                original_y = y - delta_y
                
                print(f"Найдено правильное сочетание: {original_x}x{original_y}")
                print(f"Секретный код: {result}")
                result_code = result
                found = True
                break
        if found:
            break
    
    if not found:
        print("Правильное сочетание не найдено. Попробуйте увеличить дельты.")
    
    # 6. Выводим итоговый результат
    if result_code:
        print("\n" + "="*50)
        print(f"Финальный секретный код: {result_code}")
        print("="*50)

    time.sleep(2)