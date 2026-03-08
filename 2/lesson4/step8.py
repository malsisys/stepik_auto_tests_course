import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    # открываем страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # ждем пока цена станет $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # нажимаем кнопку Book
    browser.find_element(By.ID, "book").click()

    # получаем значение x
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # вводим ответ
    browser.find_element(By.ID, "answer").send_keys(y)

    # отправляем форму
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(5)
    browser.quit()