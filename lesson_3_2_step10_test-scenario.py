from selenium import webdriver
import time
import math

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number" 

if __name__ == "__main__":
    test_abs1()
    print("All tests passed!")
    
def test_abs2():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs3():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs2()
    test_abs3()
    print("Everything passed")

    
# не забываем оставить пустую строку в конце файла