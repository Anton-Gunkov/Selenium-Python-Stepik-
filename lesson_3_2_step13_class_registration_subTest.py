# 1) Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
# 2) Создайте новый файл
# 3) Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
# 4) Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
# 5) Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
# 6) Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
# 7) Запустите получившиеся тесты из файла 
# 8) Просмотрите отчёт о запуске и найдите последнюю строчку 
# 9) Отправьте эту строчку в качестве ответа на это задание 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium import webdriver
from random import choice

import string
import time
import math
import unittest

def GenRandomLine(length=5, chars=string.ascii_lowercase + string.digits):
    return ''.join([choice(chars) for i in range(length)])

class TestRegForm(unittest.TestCase):

    # setUp() and tearDown() methods 
    # to define instructions that will be executed 
    # before and after each test method
    def setUp(self):
        options = Options()
        # браузер в режим без заголовка
        #options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
        #browser.maximize_window()
        self.browser = browser
        welcome_text = "some text"

    def tearDown(self):
        self.browser.quit()
    
    def test_Regs_all(self):
        browser = self.browser
        urls = ["http://suninjuly.github.io/registration1.html",
                "http://suninjuly.github.io/registration2.html"]
        # используем subTest
        for url in urls:
            with self.subTest(url=url):
                browser.get(url)
                browser.find_element(By.CSS_SELECTOR, "input.first:required").send_keys(GenRandomLine())
                browser.find_element(By.CSS_SELECTOR, "input.second:required").send_keys(GenRandomLine())
                browser.find_element(By.CSS_SELECTOR, "input.third:required").send_keys(GenRandomLine())
                # Отправляем заполненную форму
                browser.find_element(By.CSS_SELECTOR, "button.btn").click()
                # ждем загрузки ответа        
                WebDriverWait(browser, 5).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Congratulations! You have successfully registered!"))
                # записываем в переменную welcome_text текст из элемента
                welcome_text = browser.find_element(By.TAG_NAME, "h1").text
                # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
                self.assertEqual(welcome_text, 
                                "Congratulations! You have successfully registered!", 
                                " :-( NOT REGISTERED" )
                
if __name__ == "__main__":
    unittest.main()
    
# не забываем оставить пустую строку в конце файла