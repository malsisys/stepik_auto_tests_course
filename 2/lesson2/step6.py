import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# функция вычисления
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    # открываем страницу
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # получаем значение x
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # скроллим страницу до поля ввода
    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("arguments[0].scrollIntoView(true);", answer)

    # вводим ответ
    answer.send_keys(y)

    # отмечаем checkbox и radiobutton
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    # нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # время чтобы скопировать код из alert
    time.sleep(30)
    browser.quit()