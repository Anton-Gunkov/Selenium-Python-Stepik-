from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import pytest
#import unittest
import time
import math

browser = webdriver.Chrome()

link = "https://stepik.org/lesson/236898/step/1"
browser.get(link)
browser.implicitly_wait(10)
msg_elemnt = ""

browser.find_element(By.CSS_SELECTOR, "a[id='ember33']").click()
browser.find_element(By.CSS_SELECTOR, "input[id='id_login_email']").send_keys("XXXXXXXXXXXX@xxxxxxxx.xxx")
browser.find_element(By.CSS_SELECTOR, "input[id='id_login_password']").send_keys("XXXXXXXXXXXXXXXX")
browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
browser.refresh()

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea:required")))
browser.find_element(By.CSS_SELECTOR, "textarea:required").send_keys(math.log(int(time.time())))
WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='submit-submission']")))
#browser.find_element(By.CSS_SELECTOR, "button[class='again-btn white']").click()
browser.find_element(By.CSS_SELECTOR, "button[class='submit-submission']").click()
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p[class='smart-hints__hint']")))
msg_elemnt = browser.find_element(By.CSS_SELECTOR, "p[class='smart-hints__hint']").text

assert msg_elemnt == str("Correct!"), f"\n{msg_elemnt}"

WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class='again-btn white']")))
browser.find_element(By.CSS_SELECTOR, "button[class='again-btn white']").click()

print(f"\n{msg_elemnt}")
browser.quit()


