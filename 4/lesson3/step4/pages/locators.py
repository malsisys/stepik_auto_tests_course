from selenium.webdriver.common.by import By


class ProductPageLocators:
    # кнопка добавления товара в корзину
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    # название товара на странице
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")

    # цена товара на странице
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    # сообщение об успешном добавлении товара
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        "#messages .alert-success strong"
    )

    # сообщение со стоимостью корзины
    BASKET_TOTAL = (
        By.CSS_SELECTOR,
        "#messages .alert-info strong"
    )