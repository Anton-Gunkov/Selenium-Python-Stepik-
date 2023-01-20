from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from random import choice
import string

def GenRandomLine(length=5, chars=string.ascii_lowercase + string.digits):
    return ''.join([choice(chars) for i in range(length)])

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys(GenRandomLine())

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    print(browser.switch_to.alert.text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла