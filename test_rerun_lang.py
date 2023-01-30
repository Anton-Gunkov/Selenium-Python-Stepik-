#import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py
# параметр "--tb=line", чтобы сократить лог с результатами теста

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")
    