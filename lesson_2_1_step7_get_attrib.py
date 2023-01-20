from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "     http://suninjuly.github.io/get_attribute.html    "

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "img[id='treasure']").get_attribute("valuex")
    y = calc(x)
    
    # ОТЛАДКА - код в консоль
    print(x, y)

    browser.find_element(By.ID, "answer").send_keys(calc(x))

    # checkbox "I'm the robot"
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox:required").click()
    
    # radiobutton "Robots rule!"
    browser.find_element(By.CSS_SELECTOR, "input[id ='robotsRule']").click()
    
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()
    
# не забываем оставить пустую строку в конце файла