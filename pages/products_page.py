from pages.cart_page import CartPage
from pages.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.product_list = page.locator(".inventory_item")
        self.add_cart = page.locator("[id^='add-to-cart']")
        self.product_name = page.locator(".inventory_item_name")
        self.product_price = page.locator(".inventory_item_price")
        self.cart_icon = page.locator(".shopping_cart_link")

    def add_product_in_cart(self, product_name):
        product = self.product_list.filter(
            has_text=product_name
        )
        product.locator(self.add_cart).click()
        return "Product added to cart"

    def get_price(self, product_name):
        price = self.page.locator(self.product_name).filter(
            has_text=product_name
        )
        return product.locator(self.product_price).text_content()

    def click_cart_icon(self):
        self.click(self.cart_icon)
        cart_page = CartPage(self.page)
        return cart_page
