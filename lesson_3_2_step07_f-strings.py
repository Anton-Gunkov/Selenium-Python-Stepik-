from selenium import webdriver
import time
import math

try:
    actual_result = "abrakadabra"
    print("Wrong text, got " + actual_result + ", something wrong")
    
    print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))
    
    actual_result = "abrakadabra"
    print(f"Wrong text, got '{actual_result}', something wrong")
    
    str1 = "one"
    str2 = "two"
    str3 = "three"
    print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")
    
    print(f"Simple 2 x 2 = {2*2}")
    
except Exception as error:
    print(f'ОШИБКА: {error}')

finally:
    time.sleep(1)
    
# не забываем оставить пустую строку в конце файла