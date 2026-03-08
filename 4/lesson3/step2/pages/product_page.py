from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        # нажимаем кнопку добавления товара в корзину
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_added_product_name(self):
        # получаем название товара со страницы
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text

        # получаем название товара из сообщения об успехе
        success_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE
        ).text

        # сравниваем названия
        assert product_name == success_name, (
            f"Expected product name '{product_name}', but got '{success_name}'"
        )

    def should_be_product_price_in_basket(self):
        # получаем цену товара со страницы
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text

        # получаем стоимость корзины из сообщения
        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
        ).text

        # сравниваем цену товара и стоимость корзины
        assert product_price == basket_total, (
            f"Expected basket total '{product_price}', but got '{basket_total}'"
        )