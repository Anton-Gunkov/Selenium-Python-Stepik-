from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # для получения текста из <a>ТЕКСТ</a> используется .text без скобок
    # затем преобразуем текст в числа
    x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
    
    browser.find_element(By.ID, "answer").send_keys(calc(x))

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # checkbox "I'm the robot"
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox:required").click()
    
    # radiobutton "Robots rule!"
    browser.find_element(By.CSS_SELECTOR, "input[id ='robotsRule']").click()
    
    #browser.find_element(By.XPATH, "//button[text()='Submit']").click()

    button.click()

    print(browser.switch_to.alert.text)

except Exception as error:
    print(f'ОШИБКА: {error}')

finally:
    time.sleep(3)
    browser.quit()
    
# не забываем оставить пустую строку в конце файла