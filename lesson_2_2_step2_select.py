from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.chrome.options import Options
import warnings

warnings.filterwarnings("ignore", category = DeprecationWarning)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])

#link = "https://suninjuly.github.io/selects1.html"
link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # для получения текста из <a>ТЕКСТ</a> используется .text без скобок
    # затем преобразуем текст в числа
    x = int(browser.find_element(By.CSS_SELECTOR, "span[id='num1']").text)
    y = int(browser.find_element(By.CSS_SELECTOR, "span[id='num2']").text)
        
    # ОТЛАДКА - код в консоль
    print(x, y, x + y)

    # поиск и выбор в выпадающем списке, Select с большой буквы. Числа обратно -> в текст
    Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(str(x + y))
    
    # жмак кнопку
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()
    
# не забываем оставить пустую строку в конце файла