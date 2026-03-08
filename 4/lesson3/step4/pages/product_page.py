from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        # нажимаем кнопку добавления товара в корзину
        self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        ).click()

    def get_product_name(self):
        # получаем название товара со страницы товара
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text

    def get_product_price(self):
        # получаем цену товара со страницы товара
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text

    def should_be_added_product_name(self, product_name):
        # получаем название товара из сообщения после добавления в корзину
        success_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE
        ).text

        # проверяем, что название в сообщении совпадает с ожидаемым
        assert product_name == success_name, (
            f"Expected product name '{product_name}', but got '{success_name}'"
        )

    def should_be_product_price_in_basket(self, product_price):
        # получаем стоимость корзины из сообщения
        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
        ).text

        # проверяем, что стоимость корзины совпадает с ценой товара
        assert product_price == basket_total, (
            f"Expected basket total '{product_price}', but got '{basket_total}'"
        )