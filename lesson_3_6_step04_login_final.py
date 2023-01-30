from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import time
import math

url1 = "236895/step/1"
url2 = "236897/step/1"
url3 = "236898/step/1"
url4 = "236899/step/1"
url5 = "236903/step/1"
url6 = "236904/step/1"
url7 = "236905/step/1"

#final_txt = "" 

@pytest.mark.parametrize('url', [url1, url2, url3, url4, url5, url6, url7])
class TestUFO:
    def test_I_am_should_login(self, browser, url):
        link = f"https://stepik.org/lesson/{url}"
        browser.get(link)
        browser.implicitly_wait(10)
        msg_elemnt = ""

        browser.find_element(By.CSS_SELECTOR, "a[id='ember33']").click()
        browser.find_element(By.CSS_SELECTOR, "input[id='id_login_email']").send_keys("xxxxxxxxxxxxxxx@xxxxxxxxxx.xxx")
        browser.find_element(By.CSS_SELECTOR, "input[id='id_login_password']").send_keys("xxxxxxxxxxxxxx")
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
        
        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class='again-btn white']")))
        browser.find_element(By.CSS_SELECTOR, "button[class='again-btn white']").click()
        
        #assertEqual(msg_elemnt, "Correct!", f"{msg_elemnt}")
        
        try:
            assert "Correct!" in msg_elemnt
        except:
            with open("3_6_5_test_Errors.log", "a") as f:
                f.write(msg_elemnt)
            raise AssertionError('Error! See "3_6_5_test_Errors.log"')

