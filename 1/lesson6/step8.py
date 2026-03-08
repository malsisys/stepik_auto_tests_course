from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    # открываем страницу с формой
    browser.get("http://suninjuly.github.io/find_xpath_form")

    # заполняем поля формы
    browser.find_element(By.NAME, "first_name").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")

    # находим кнопку именно с текстом Submit через XPath
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # даем время скопировать код из alert
    time.sleep(30)
    browser.quit()