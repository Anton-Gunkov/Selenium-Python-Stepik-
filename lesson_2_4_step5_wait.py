from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)



try:
    browser.get("http://suninjuly.github.io/wait1.html")

    browser.find_element(By.ID, "verify").click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
    print(message.text)

except Exception as error:
    print(f'ОШИБКА: {error}')

finally:
    #    time.sleep(3)
    browser.quit()
    
# не забываем оставить пустую строку в конце файла