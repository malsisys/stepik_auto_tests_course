from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    # ссылка на страницу товара с promo-параметром
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    # создаем объект страницы товара и открываем страницу
    page = ProductPage(browser, link)
    page.open()

    # добавляем товар в корзину
    page.add_product_to_basket()

    # решаем промо-капчу и получаем код в консоли
    page.solve_quiz_and_get_code()

    # проверяем, что в сообщении указано правильное название товара
    page.should_be_added_product_name()

    # проверяем, что цена товара совпадает со стоимостью корзины
    page.should_be_product_price_in_basket()