from pages.cart_page import CartPage
from constants.product_selectors import ProductSelectors
from pages.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def add_product_in_cart(self, product_name):
        product = self.page.locator(ProductSelectors.PRODUCT_LIST).filter(
            has_text=product_name
        )
        product.locator(ProductSelectors.ADD_TO_CART).click()
        return "Product added to cart"

    def get_price(self, product_name):
        price = self.page.locator(ProductSelectors.PRODUCT_NAME).filter(
            has_text=product_name
        )
        return product.locator(ProductSelectors.PRODUCT_PRICE).text_content()

    def click_cart_icon(self):
        self.page.click(ProductSelectors.CART_ICON)
        cart_page = CartPage(self.page)
        return cart_page
