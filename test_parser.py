import pytest
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

# pytest -s -v --browser_name=chrome test_parser.py

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")