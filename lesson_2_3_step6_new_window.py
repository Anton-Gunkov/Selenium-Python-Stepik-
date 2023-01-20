from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # переключимся на вторую вкладку
    #calc_window = browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    print(browser.switch_to.alert.text)
    browser.switch_to.alert.accept()

except Exception as error:
    print(f'ОШИБКА: {error}')

finally:
    #    time.sleep(3)
    browser.quit()
    
# не забываем оставить пустую строку в конце файла