from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element(By.ID, "peopleRule")

    print(people_radio.get_attribute("name"))
    # Напечатает ruler, т.е. текстовое значение аттрибута

    print(people_radio.get_attribute("checked"))
    # Напечатает true, т.е. факт того что аттрибут существует. Учтите что true это в данном случае строка, а не булево значение.

    print(people_radio.get_attribute("href"))
    # Напечатает None, т.к. аттрибут не существует. И это не строка а None-значение.

    #Проверяем зачение атрибута "required" у "I'm the robot".
    people_radio = browser.find_element(By.ID, "robotCheckbox")
    the_robot = people_radio.get_attribute("required")
    print("value of I'm the robot:", the_robot)
    assert the_robot is not None, "the_robot is not selected by default"

    #Проверяем значение атрибута "checked" у "People rule".
    people_checked = browser.find_element(By.ID, "peopleRule")
    people_rule = people_checked.get_attribute("checked")
    print("value of People rule:", people_rule)
    assert people_rule is not None, "people_rule is not selected by default"

    #Проверяем значение "checked" у "Robots rule".
    robot_checked = browser.find_element(By.ID, "robotsRule")
    robot_rule = robot_checked.get_attribute("checked")
    print("value of Robot rule:", robot_rule)
    assert robot_rule is None, "robot_rule is not selected by default"

    #Проверяем значение "disabled" у "Submit".
    submit_checked = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_disabled = submit_checked.get_attribute("disabled")
    print("value of button Submit:", submit_disabled)
    assert submit_disabled is None

    #Проверяем значение "disabled" у "Submit" спустя - 10 секунд.
    time.sleep(10)
    submit_disabled = submit_checked.get_attribute("disabled")
    print("value of button Submit after TEN seconds:", submit_disabled)
    assert submit_disabled is not None

finally:
    time.sleep(3)
    browser.quit()
    
# не забываем оставить пустую строку в конце файла