from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element(By.CSS_SELECTOR, "input[name='firstname']:required").send_keys("AaaA")
    browser.find_element(By.CSS_SELECTOR, "input[name='lastname']:required").send_keys("BbbB")
    browser.find_element(By.CSS_SELECTOR, "input[name='email']:required").send_keys("a@b.c")

    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)

    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'freestyler.txt')           
    print(file_path)

    browser.find_element(By.CSS_SELECTOR, "input[id='file']").send_keys(file_path)

    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

    print(browser.switch_to.alert.text)

except Exception as error:
    print(f'ОШИБКА: {error}')

finally:
    # ОК алерт
    time.sleep(1)
    #Alert(browser).accept()
    browser.quit()
    
# не забываем оставить пустую строку в конце файла