from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('url', [
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_add_to_cart(browser, url):
    page = ProductPage(browser, url)
    page.open()
    text_name_product = page.get_name_product()
    text_price_product = page.get_price_product()
    page.click_button_cart()
    text_name_product_in_cart = page.get_name_product_in_cart()
    text_price_product_in_cart = page.get_price_product_in_cart()
    assert text_name_product == text_name_product_in_cart
    assert text_price_product == text_price_product_in_cart
