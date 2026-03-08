import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        # открываем первую страницу регистрации
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        # заполняем обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test@test.com")

        # отправляем форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # проверяем текст успешной регистрации
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        # закрываем браузер
        browser.quit()

    def test_registration2(self):
        # открываем вторую страницу регистрации
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        # заполняем обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test@test.com")

        # отправляем форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # проверяем текст успешной регистрации
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        # закрываем браузер
        browser.quit()


if __name__ == "__main__":
    unittest.main()