from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap").text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(calc(x))

    # вариант 1 - клик по checkbox c id="robotCheckbox"
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox:required").click()
    
    # вариант 2 - клик по radiobutton label c for="robotsRule"
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    print(browser.switch_to.alert.text)

    # ОТЛАДКА - код в консоль
    print(x, y)

except Exception as error:
    print(f'Произошла ошибка: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла