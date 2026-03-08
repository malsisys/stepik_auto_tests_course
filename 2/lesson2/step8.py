from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()

try:
    # открываем страницу
    browser.get("http://suninjuly.github.io/file_input.html")

    # заполняем поля формы
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("test@test.com")

    # создаем путь к файлу test.txt в текущей папке
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test.txt")

    # загружаем файл
    browser.find_element(By.ID, "file").send_keys(file_path)

    # нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # время чтобы скопировать код
    time.sleep(30)
    browser.quit()