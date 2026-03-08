from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    # открываем страницу товара по новой ссылке
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()

    # заранее сохраняем название и цену товара со страницы
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    # добавляем товар в корзину
    page.add_product_to_basket()

    # решаем промо-капчу
    page.solve_quiz_and_get_code()

    # проверяем название товара в сообщении
    page.should_be_added_product_name(product_name)

    # проверяем цену товара в корзине
    page.should_be_product_price_in_basket(product_price)