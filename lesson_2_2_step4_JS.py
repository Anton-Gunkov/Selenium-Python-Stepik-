from selenium import webdriver
from selenium.webdriver.common.alert import Alert

import time

link = "http://ya.ru"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    # главное, кавычки 
    # и порядок действий
    browser.execute_script('document.title="Script executing";')

    browser.execute_script("alert('Robots at work');")
    time.sleep(1)

    # ОК алерт
    Alert(browser).accept()
    time.sleep(1)

    browser.execute_script("document.title='NEW Script executing';alert('NEW Robots at work');")

except Exception as error:
    print(f'ОШИБКА: {error}')

finally:
    time.sleep(2)
    Alert(browser).accept()
    time.sleep(1)
    browser.quit()
    
# не забываем оставить пустую строку в конце файла