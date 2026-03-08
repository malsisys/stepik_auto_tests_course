import math
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException


class BasePage:
    def __init__(self, browser, url):
        # сохраняем браузер и ссылку страницы
        self.browser = browser
        self.url = url

    def open(self):
        # открываем нужную страницу
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        # проверяем, что элемент есть на странице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        # переключаемся на alert и достаем число для вычисления
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]

        # считаем ответ и отправляем его в alert
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()

        # если появляется второй alert с кодом — печатаем его
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")