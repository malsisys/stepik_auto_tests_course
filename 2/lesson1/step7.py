import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# функция для вычисления
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    # открываем страницу
    browser.get("http://suninjuly.github.io/get_attribute.html")

    # находим картинку сундука и получаем значение атрибута
    chest = browser.find_element(By.ID, "treasure")
    x = chest.get_attribute("valuex")

    # считаем значение функции
    y = calc(x)

    # вводим результат
    browser.find_element(By.ID, "answer").send_keys(y)

    # отмечаем чекбокс
    browser.find_element(By.ID, "robotCheckbox").click()

    # выбираем радиокнопку
    browser.find_element(By.ID, "robotsRule").click()

    # нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # время чтобы скопировать код
    time.sleep(30)
    browser.quit()