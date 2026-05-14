from pages.base_page import BasePage
from pages.products_page import ProductsPage
from constants.login_selectors import LoginSelectors



class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def login(self, username, password):
        self.fill(LoginSelectors.USERNAME, username)
        self.fill(LoginSelectors.PASSWORD, password)
        self.click(LoginSelectors.SUBMIT)
        products_page = ProductsPage(self.page)
        return products_page
