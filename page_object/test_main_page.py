import time

from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

def test_guest_should_see_login_link(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasePage(browser, url)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasePage(browser, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, url)
    login_page.should_be_login_page()

def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com/ru/"
    page = BasePage(browser, url)
    page.open()
    page.go_to_cart()
    url_basket = browser.current_url
    assert '/ru/basket/' in url_basket
    basketpage = BasketPage(browser, url='http://selenium1py.pythonanywhere.com/ru/basket/')
    basketpage.check_status_basket_for_empty()

def  test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
    page = ProductPage(browser, url)
    page.open()
    page.click_first_item()
    page.go_to_cart()
    url_basket = browser.current_url
    assert '/ru/basket/' in url_basket
    basketpage = BasketPage(browser, url='http://selenium1py.pythonanywhere.com/ru/basket/')
    basketpage.check_status_basket_for_empty()