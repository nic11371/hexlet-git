import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.options import Options

solver = TwoCaptcha('')
dict_result = {}
img_name = 'img.png'


def sender_solve(path=img_name):
    print('2) Изображение отправлено для разгадывания:')
    result = solver.normal(path)
    print('3) От API пришёл ответ:', result)
    dict_result.update(result)
    return result.get('code')


def check_captcha(browser):
    """Универсальная функция проверки и решения капчи"""
    try:
        # Проверяем наличие капчи без вызова исключения
        if 'Подтвердите, что вы не робот' not in browser.page_source:
            return True  # Капчи нет, продолжаем работу

        print("Обнаружена капча, начинаем решение...")
        browser.find_element(
            By.CSS_SELECTOR, 'div[class="chakra-form-control css-1sx6owr"]'
        ).find_element(By.TAG_NAME, 'img').screenshot(img_name)
        print('1) Скриншот области успешно сделан')

        captcha_text = sender_solve()
        browser.find_element(By.ID, 'field-:r0:').send_keys(captcha_text)
        browser.find_element(
            By.CSS_SELECTOR, 'button[class="chakra-button css-1wq39mj"]'
        ).click()

        # Проверяем успешность решения
        time.sleep(2)  # Даем время на обработку
        if 'Подтвердите, что вы не робот' not in browser.page_source:
            solver.report(dict_result['captchaId'], True)
            print(f"Капча успешно решена. ID: {dict_result['captchaId']}")
            return True

        print("Капча не решена, пробуем еще раз")
        solver.report(dict_result['captchaId'], False)
        return False

    except Exception as e:
        print(f"Ошибка при обработке капчи: {e}")
        return False


def get_products(browser):
    return [x.text for x in browser.find_elements(By.CLASS_NAME, 'css-5ev4sb')]


chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('https://captcha-parsinger.ru/')
    pagination_btns = browser.find_elements(By.CSS_SELECTOR, "li.css-k008qs")
    pages = sorted(list({btn.text for btn in pagination_btns if btn.text.isdigit()}))

    articles = []
    for page in pages:
        browser.get(f"https://captcha-parsinger.ru/?page={page}")

        # Проверяем и решаем капчу если нужно
        if not check_captcha(browser):
            print("Не удалось решить капчу, пропускаем страницу")
            continue  # Переходим к следующей странице

        # Парсим артикулы
        items = browser.find_elements(By.CLASS_NAME, 'css-1ecvsm5')
        for item in items:
            try:
                article_element = item.find_element(By.XPATH, './/li[contains(text(), "Артикул:")]')
                article = article_element.text.split(":")[1].strip()
                articles.append(int(article))
            except Exception as e:
                print(f"Ошибка при парсинге артикула: {e}")

    print(f"Итоговая сумма артикулов: {sum(articles)}")
