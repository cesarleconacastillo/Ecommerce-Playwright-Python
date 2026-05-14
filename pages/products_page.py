from pages.cart_page import CartPage
from constants.product_selectors import ProductSelectors
from pages.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def get_products_list(self):
        return self.page.locator(".inventory_list .inventory_item")
        #return self.page.list_locator(ProductSelectors.PRODUCT_LIST)

    def add_product_in_cart(self, product_name, product_list):
        for i in range(product_list.count()):
            product = product_list.nth(i)
            name = product.locator(ProductSelectors.PRODUCT_NAME).text_content()
            if name == product_name:
                product.locator(ProductSelectors.ADD_TO_CART).click()
                return "Product added to cart"
        return "Product not found"

    def get_price(self, product_name, product_list):
        price = ""
        for i in range(product_list.count()):
            product = product_list.nth(i)
            name = product.locator(ProductSelectors.PRODUCT_NAME).text_content()
            if name == product_name:
                price = product.locator(ProductSelectors.PRODUCT_PRICE).text_content()
        return price

    def click_cart_icon(self):
        self.page.click(ProductSelectors.CART_ICON)
        cart_page = CartPage(self.page)
        return cart_page

