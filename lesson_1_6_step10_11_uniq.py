from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from random import choice
import string

def GenRandomLine(length=5, chars=string.ascii_lowercase + string.digits):
    return ''.join([choice(chars) for i in range(length)])

try: 
    #URL = "http://suninjuly.github.io/registration1.html"
    URL = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(URL)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, "input.first:required").send_keys(GenRandomLine())
    browser.find_element(By.CSS_SELECTOR, "input.second:required").send_keys(GenRandomLine())
    browser.find_element(By.CSS_SELECTOR, "input.third:required").send_keys(GenRandomLine())

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

except Exception as error:
    print(f'ОШИБКА: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла