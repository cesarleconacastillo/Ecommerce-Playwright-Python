from constants.cart_selectors import CartSelectors
from pages.checkout_page import CheckoutPage
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def get_qty(self):
        return self.get_text(CartSelectors.QUANTITY)

    def get_name(self):
        return self.get_text(CartSelectors.PRODUCT_NAME)

    def get_price(self):
        return self.get_text(CartSelectors.PRODUCT_PRICE)

    def go_to_checkout(self):
        self.page.click(CartSelectors.CHECKOUT_BTN)
        checkout_page = CheckoutPage(self.page)
        return checkout_page