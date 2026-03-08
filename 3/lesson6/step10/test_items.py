from selenium.webdriver.common.by import By


def test_guest_should_see_add_to_basket_button(browser):
    # открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # ищем кнопку добавления в корзину
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    # проверяем, что кнопка есть на странице
    assert button is not None, "Add to basket button is not present"