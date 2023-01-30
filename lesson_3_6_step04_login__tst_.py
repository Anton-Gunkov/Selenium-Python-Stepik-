from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import unittest
import time
import math

link = "https://stepik.org/lesson/236905/step/1"

class TestUFO(unittest.TestCase):
    def test_I_am_should_login(self):
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(10)
        msg_elemnt = ""

        browser.find_element(By.CSS_SELECTOR, "a[id='ember33']").click()
        browser.find_element(By.CSS_SELECTOR, "input[id='id_login_email']").send_keys("XXXXXXXXXXXXXX@x.x")
        browser.find_element(By.CSS_SELECTOR, "input[id='id_login_password']").send_keys("XXXXXXXXXXXXXXX")
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        browser.refresh()

        WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea:required")))
        browser.find_element(By.CSS_SELECTOR, "textarea:required").send_keys(math.log(int(time.time())))
        WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='submit-submission']")))
        #browser.find_element(By.CSS_SELECTOR, "button[class='again-btn white']").click()
        browser.find_element(By.CSS_SELECTOR, "button[class='submit-submission']").click()
        WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p[class='smart-hints__hint']")))
        msg_elemnt = browser.find_element(By.CSS_SELECTOR, "p[class='smart-hints__hint']").text
        #print(f"\n{msg_elemnt}")
        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class='again-btn white']")))
        browser.find_element(By.CSS_SELECTOR, "button[class='again-btn white']").click()
        
        self.assertEqual(msg_elemnt, "sCorrect!", f"{msg_elemnt}")
        
        #try:
        #    assert "Correct!" in msg_elemnt
        #except:
        #    with open("3_6_5_test_Errors.log", "a") as f:
        #        f.write(msg_elemnt)
        #    raise AssertionError('Error! See "3_6_5_test_Errors.log"')
        
        #try:
        #    assert msg_elemnt == "Correct!"
        #except AssertionError:
        #    final_txt += msg_elemnt  # собираем ответ про Сов с каждой ошибкой
#print(final_txt)
        
        #assert str(msg_elemnt) == str("Correct!"), f"\n{msg_elemnt}"

if __name__ == "__main__":
    unittest.main()
    
# не забываем оставить пустую строку в конце файла