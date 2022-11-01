from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

def test_guest_should_see_login_link(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.click_button_cart()