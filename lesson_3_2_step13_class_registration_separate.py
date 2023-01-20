# 1) Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
# 2) Создайте новый файл
# 3) Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
# 4) Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
# 5) Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
# 6) Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
# 7) Запустите получившиеся тесты из файла 
# 8) Просмотрите отчёт о запуске и найдите последнюю строчку 
# 9) Отправьте эту строчку в качестве ответа на это задание  FAILED (errors=1)
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common import exceptions
from selenium import webdriver
from random import choice

import string
import time
import math
import unittest

def GenRandomLine(length=5, chars=string.ascii_lowercase + string.digits):
    return ''.join([choice(chars) for i in range(length)])

browser = webdriver.Chrome()

class TestRegForm(unittest.TestCase):
    
    # setUp() and tearDown() methods
    # to define instructions that will be executed 
    # before and after each test method""
    def setUp(self):
        result = "some result"

    #def tearDown(self):
        #time.sleep(1)
        # close() валит всё
        #browser.close()
        #browser.switch_to.window(browser.window_handles[1])
        
    def fill_form(self, url):
        #  Вспомогательный метод для заполнения форм
        browser.switch_to.new_window('tab')
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
        result = browser.find_element(By.TAG_NAME, "h1").text
        return result
 
    def test_registration1(self):
        form_url = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(form_url)
        self.assertEqual(registration_result, 
                        "Congratulations! You have successfully registered!", 
                        " :-( NOT REGISTERED" )    
        
    def test_registration2(self):
        form_url = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(form_url)
        self.assertEqual(registration_result, 
                        "Congratulations! You have successfully registered!", 
                        " :-( NOT REGISTERED" )            
        
if __name__ == "__main__":
    unittest.main()
    
# не забываем оставить пустую строку в конце файла