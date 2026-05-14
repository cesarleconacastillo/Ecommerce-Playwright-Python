import time
from threading import Thread

from fixtures.data import login_data, product_data, cart_data, checkout_data
from pages.login_page import LoginPage
from constants.urls import BASE_URL


def test_login(page, login_data, product_data, cart_data, checkout_data):
    # Login
    login_page = LoginPage(page)
    login_page.goto(BASE_URL)
    username = login_data["valid_user"]["username"]
    password = login_data["valid_user"]["password"]
    products = login_page.login(username, password)
    # Products
    product_list = products.get_products_list()
    product_name = product_data["product"]["name"]
    result = products.add_product_in_cart(product_name, product_list)
    print(result)

    #Cart
    cart_page = products.click_cart_icon()

    expected_qty = cart_data["cart"]["quantity"]
    expected_name = cart_data["cart"]["name"]
    expected_price = cart_data["cart"]["price"]

    assert cart_page.get_qty() == expected_qty
    assert cart_page.get_name() == expected_name
    assert cart_page.get_price() == expected_price

    # Checkout
    checkout_page = cart_page.go_to_checkout()
    first_name = checkout_data["checkout"]["first_name"]
    last_name = checkout_data["checkout"]["last_name"]
    zip_code = checkout_data["checkout"]["zip_code"]

    checkout_page.fill_data(first_name, last_name, zip_code)
    checkout_page.click_continue()
    checkout_page.confirm_checkout()

    confirmation_msg = checkout_page.order_placed()
    expected_conf_msg = checkout_data["checkout"]["conf_msg"]
    assert confirmation_msg == expected_conf_msg











