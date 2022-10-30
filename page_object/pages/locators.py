from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(BasePage):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BUTTON_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_PRODUCT = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRICE_PRODUCT = (By.CLASS_NAME, "price_color")
    NAME_PRODUCT_IN_CART = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRICE_PRODUCT_IN_CART = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')