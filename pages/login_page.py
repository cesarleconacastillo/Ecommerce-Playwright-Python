from pages.base_page import BasePage
from pages.products_page import ProductsPage



class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.submit_button = page.locator("#login-button")

    def login(self, username, password):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.submit_button)
        return ProductsPage(self.page)
