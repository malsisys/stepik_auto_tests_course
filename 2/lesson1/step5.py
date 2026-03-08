import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# функция для вычисления значения
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    # открываем страницу
    browser.get("https://suninjuly.github.io/math.html")

    # получаем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # вычисляем результат
    y = calc(x)

    # вводим ответ в поле
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # отмечаем чекбокс
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # выбираем радиокнопку
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()