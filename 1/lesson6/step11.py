import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        # Чтобы проверить, что тест "ловит" баг, поменяйте ссылку на:
        # link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        try:
            browser.get(link)

            # Уникальные селекторы: поля именно из блока first_block
            first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input")
            last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input")
            email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input")

            first_name.send_keys("Ivan")
            last_name.send_keys("Petrov")
            email.send_keys("ivan.petrov@example.com")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем успешную регистрацию
            welcome_text = browser.find_element(By.TAG_NAME, "h1").text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()