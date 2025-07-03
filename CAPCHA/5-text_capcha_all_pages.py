import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.options import Options


articles_pages = []


def solver(question):
    solver = TwoCaptcha('')
    print('Вопрос отправился на решение:', question)
    result = solver.text(question)
    print('От API пришёл ответ: ', result)
    return result['code']


def solution_capcha(browser):
    time.sleep(2)
    question_text = browser.find_element(
        By.CSS_SELECTOR, 'div[class="chakra-form-control css-1sx6owr"]').find_element(
        By.TAG_NAME, 'p').text
    tag_input = browser.find_element(By.ID, 'field-:r0:')
    tag_input.send_keys(solver(question_text))
    elem_button = browser.find_element(
        By.CSS_SELECTOR, 'button[class="chakra-button css-1wq39mj"]')
    elem_button.click()
    return question_text, elem_button


def result_solution_capcha(question_text, elem_button):
    while True:
        name_card = [x.text for x in browser.find_elements(
            By.CLASS_NAME, 'css-5ev4sb')]
        if len(name_card) > 0:
            print('Решение верное, данные получены')
            return True
        else:
            print('Решение неверное, ещё попытка')
            browser.find_element(
                By.ID, 'field-:r0:').send_keys(solver(question_text))
            elem_button.click()
            time.sleep(1)
            [name_card.append(x.text) for x in browser.find_elements(
                By.CLASS_NAME, 'css-5ev4sb')]


def parcing_page(browser):
    articles = []
    items = browser.find_elements(By.CLASS_NAME, 'css-1ecvsm5')
    for a in items:
        atricle_element = a.find_element(By.XPATH, './/li[contains(text(), "Артикул:")]')
        article = atricle_element.text.split(":")[1].strip()
        articles.append(int(article))
    return sum(articles)


chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')


with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('https://captcha-parsinger.ru/text')
    pagination_btns = browser.find_elements(By.CSS_SELECTOR, "li.css-k008qs")
    pages = sorted(
        list({btn.text for btn in pagination_btns if btn.text.isdigit()}))

    articles = []
    for page in pages:
        browser.get(f"https://captcha-parsinger.ru/text?page={page}")
        if 'Подтвердите, что вы не робот' in browser.page_source:
            browser.get('https://captcha-parsinger.ru/text?page=3')
            question_text, elem_button = solution_capcha(browser)
            time.sleep(1)
            result = result_solution_capcha(question_text, elem_button)
            if result:
                articles_pages.append(int(parcing_page(browser)))
        else:
            articles_pages.append(int(parcing_page(browser)))
    print(sum(articles_pages))
