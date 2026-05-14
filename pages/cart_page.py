from pages.checkout_page import CheckoutPage
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.quantity = page.locator(".cart_quantity")
        self.product_name = page.locator(".inventory_item_name")
        self.product_price = page.locator(".inventory_item_price")
        self.checkout_btn = page.locator("#checkout")

    def get_qty(self):
        return self.get_text(self.quantity)

    def get_name(self):
        return self.get_text(self.product_name)

    def get_price(self):
        return self.get_text(self.product_price)

    def go_to_checkout(self):
        self.click(self.checkout_btn)
        checkout_page = CheckoutPage(self.page)
        return checkout_page