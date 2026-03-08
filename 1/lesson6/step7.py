from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # открываем браузер и страницу с формой
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # находим все обязательные поля ввода
    elements = browser.find_elements(By.TAG_NAME, "input")

    # заполняем каждое найденное поле
    for element in elements:
        element.send_keys("1")

    # находим кнопку отправки и нажимаем её
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # даём время скопировать код из всплывающего окна
    time.sleep(30)

    # закрываем браузер
    browser.quit()