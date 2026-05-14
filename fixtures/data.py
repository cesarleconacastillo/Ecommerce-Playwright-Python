import json
import pytest

@pytest.fixture(scope="session")
def login_data():
    with open('data/login_data.json') as file:
        login_data = json.load(file)
    return login_data

@pytest.fixture(scope="session")
def product_data():
    with open('data/product_data.json') as file:
        product_data = json.load(file)
    return product_data

@pytest.fixture(scope="session")
def cart_data():
    with open('data/cart_data.json') as file:
        cart_data = json.load(file)
    return cart_data

@pytest.fixture(scope="session")
def checkout_data():
    with open('data/checkout_data.json') as file:
        checkout_data = json.load(file)
    return checkout_data