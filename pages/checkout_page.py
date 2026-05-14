from constants.checkout_selectors import CheckoutSelectors
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def fill_data(self, first_name, last_name, zip_code):
        self.page.fill(CheckoutSelectors.CHECKOUT_FIRST_NAME, first_name)
        self.page.fill(CheckoutSelectors.CHECKOUT_LAST_NAME, last_name)
        self.page.fill(CheckoutSelectors.CHECKOUT_ZIP, zip_code)

    def click_continue(self):
        self.page.click(CheckoutSelectors.CONTINUE_BTN)

    def confirm_checkout(self):
        self.page.click(CheckoutSelectors.FINISH_BTN)

    def order_placed(self):
        return self.get_text(CheckoutSelectors.CONFIRMATION_MSG)
