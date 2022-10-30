from .pages.product_page import ProductPage


def test_add_to_cart(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    text_name_product = page.get_name_product()
    text_price_product = page.get_price_product()
    page.click_button_cart()
    text_name_product_in_cart = page.get_name_product_in_cart()
    text_price_product_in_cart = page.get_price_product_in_cart()
    assert text_name_product == text_name_product_in_cart
    assert text_price_product == text_price_product_in_cart
