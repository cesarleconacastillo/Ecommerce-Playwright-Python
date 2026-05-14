from pages.checkout_page import CheckoutPage
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.quantity = page.locator(".cart_quantity")
        self.product_name = page.locator(".inventory_item_name")
        self.product_price = page.locator(".inventory_item_price")
        self.checkout_btn = page.locator("#checkout")


    def validate_cart_products(
            self,
            expected_name,
            expected_price,
            expected_qty):

        actual_name = self.get_text(self.product_name)
        actual_price = self.get_text(self.product_price)
        actual_quantity = self.get_text(self.quantity)

        assert actual_name == expected_name, (
            f"Expected name '{expected_name}'"
            f"but got: '{actual_name}'"
        )

        assert actual_price == expected_price, (
            f"Expected price '{expected_price}'"
            f"but got: '{actual_price}'"
        )

        assert actual_quantity == expected_qty, (
            f"Expected quantity '{expected_qty}'"
            f"but got: '{actual_quantity}'"
        )
    """
    def get_name(self):
        return self.get_text(self.product_name)

    def get_price(self):
        return self.get_text(self.product_price)

    def actual_quantity(self):
        return self.get_text(self.quantity)
    """

    def go_to_checkout(self):
        self.click(self.checkout_btn)
        checkout_page = CheckoutPage(self.page)
        return checkout_page