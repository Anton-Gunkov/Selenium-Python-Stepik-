from selenium import webdriver
from selenium.webdriver.common.by import By

import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

try:
    browser.find_element(By.TAG_NAME, "button").click()

except Exception as error:
    print(f'ОШИБКА: {error}')

finally:
    time.sleep(3)
    browser.quit()
    
# не забываем оставить пустую строку в конце файла