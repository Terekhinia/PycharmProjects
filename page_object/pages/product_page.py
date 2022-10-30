from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def click_button_cart(self):
        button_cart = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_cart.click()
        self.solve_quiz_and_get_code()

    def get_name_product(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        return name_product.text

    def get_price_product(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        return price_product.text

    def get_name_product_in_cart(self):
        name_product_in_cart = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_CART)
        return name_product_in_cart.text

    def get_price_product_in_cart(self):
        name_price_in_cart = self.browser.find_element(*ProductPageLocators. PRICE_PRODUCT_IN_CART)
        return name_price_in_cart.text
