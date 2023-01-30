#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import unittest
import time
import math

link = "https://stepik.org/lesson/236897/step/1"

@pytest.mark.parametrize('url', [link])
class TestUFO():
    def test_I_am_should_login(self, browser, url):
        link = f"{url}"
        browser.get(link)
        browser.implicitly_wait(10)
        msg_elemnt = ""

        browser.find_element(By.CSS_SELECTOR, "a[id='ember33']").click()
        browser.find_element(By.CSS_SELECTOR, "input[id='id_login_email']").send_keys("XXXXXXXXXXXXX@xx.xx")
        browser.find_element(By.CSS_SELECTOR, "input[id='id_login_password']").send_keys("XXXXXXXXXXXXXXXX")
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        browser.refresh()

        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea:required")))
        browser.find_element(By.CSS_SELECTOR, "textarea:required").send_keys(math.log(int(time.time())))
        WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='submit-submission']")))
        #browser.find_element(By.CSS_SELECTOR, "button[class='again-btn white']").click()
        browser.find_element(By.CSS_SELECTOR, "button[class='submit-submission']").click()
        WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p[class='smart-hints__hint']")))
        msg_elemnt = browser.find_element(By.CSS_SELECTOR, "p[class='smart-hints__hint']").text

        #assert msg_elemnt == str("Correct!"), f"\n{msg_elemnt}"

        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class='again-btn white']")))
        browser.find_element(By.CSS_SELECTOR, "button[class='again-btn white']").click()

        assert msg_elemnt == str("Correct!"), f"\n{msg_elemnt}"
        # assertEqual(msg_elemnt, "Correct!", f"\n{msg_elemnt}")  
        print(f"\n{msg_elemnt}")

if __name__ == "__main__":
    unittest.main()
    
# не забываем оставить пустую строку в конце файла