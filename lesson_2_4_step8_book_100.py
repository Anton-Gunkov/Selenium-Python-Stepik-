from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

# говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.CSS_SELECTOR, "button[id='book']").click()

    x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

    print(browser.switch_to.alert.text)
    browser.switch_to.alert.accept()

except Exception as error:
    print(f'ОШИБКА: {error}')

finally:
    #   time.sleep(3)
    browser.quit()
    
# не забываем оставить пустую строку в конце файла