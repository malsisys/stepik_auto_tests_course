import time
import math
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


LINKS = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]

STEPIK_EMAIL = "vikadmitrieva07@mail.ru"
STEPIK_PASSWORD = "4WQ-a3u-eWX-5p4"


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    try:
        driver.quit()
    except Exception:
        pass


def login_via_modal(driver, wait: WebDriverWait):
    email = wait.until(EC.element_to_be_clickable((By.ID, "id_login_email")))
    password = driver.find_element(By.ID, "id_login_password")

    email.clear()
    email.send_keys(STEPIK_EMAIL)

    password.clear()
    password.send_keys(STEPIK_PASSWORD)

    driver.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

    # ВАЖНО: дождаться, что модальное затемнение исчезло (иначе клики перехватываются)
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.modal-dialog-bg")))

    # И дождаться, что поле ответа реально появилось
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea")))


def safe_click(driver, wait: WebDriverWait, locator):
    # иногда DOM перерисовывается -> stale, поэтому делаем 2 попытки
    for _ in range(2):
        try:
            btn = wait.until(EC.element_to_be_clickable(locator))
            btn.click()
            return
        except StaleElementReferenceException:
            continue
    # если всё равно stale — кликаем через JS как запасной вариант
    btn = wait.until(EC.presence_of_element_located(locator))
    driver.execute_script("arguments[0].click();", btn)


@pytest.mark.parametrize("link", LINKS)
def test_stepik_alien_message(browser, link):
    wait = WebDriverWait(browser, 30)

    browser.get(link + "?auth=login")

    # если textarea нет — логинимся
    if not browser.find_elements(By.CSS_SELECTOR, "textarea"):
        login_via_modal(browser, wait)
    else:
        # если уже залогинен, всё равно уберём возможный оверлей, если он внезапно есть
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.modal-dialog-bg")))

    textarea = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))

    answer = str(math.log(int(time.time())))
    textarea.clear()
    textarea.send_keys(answer)

    safe_click(browser, wait, (By.CSS_SELECTOR, "button.submit-submission"))

    # ХИНТ: ищем просто по классу, не привязываясь к тегу pre
    hint_el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    wait.until(lambda d: hint_el.text.strip() != "")
    hint = hint_el.text.strip()

    assert hint == "Correct!", f"Ожидали 'Correct!', но получили: {hint}"
