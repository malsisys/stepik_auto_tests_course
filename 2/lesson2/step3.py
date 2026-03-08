from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

try:
    # открываем страницу
    browser.get("https://suninjuly.github.io/selects1.html")

    # получаем значения чисел со страницы
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    # считаем сумму
    result = str(int(num1) + int(num2))

    # находим выпадающий список и выбираем нужное значение
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(result)

    # нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # время чтобы скопировать код из alert
    time.sleep(30)
    browser.quit()