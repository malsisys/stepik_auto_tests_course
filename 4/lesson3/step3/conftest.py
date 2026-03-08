import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    # создаем браузер перед тестом
    browser = webdriver.Chrome()
    yield browser

    # закрываем браузер после теста
    browser.quit()