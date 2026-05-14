from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.checkout_first_name = page.locator("#first-name")
        self.checkout_last_name = page.locator("#last-name")
        self.checkout_zip = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.confirmation_msg = page.locator(".complete-header")

    def fill_data(self, first_name, last_name, zip_code):
        self.fill(self.checkout_first_name, first_name)
        self.fill(self.checkout_last_name, last_name)
        self.fill(self.checkout_zip, zip_code)

    def click_continue(self):
        self.click(self.continue_button)

    def confirm_checkout(self):
        self.click(self.finish_button)

    def order_placed(self):
        return self.get_text(self.confirmation_msg)

    def validate_order_placed(
            self,
            expected_confirm_msg
        ):

        actual_message = self.get_text(self.confirmation_msg)

        assert expected_confirm_msg == actual_message, (
            f"Expected message '{expected_confirm_msg}'"
            f"but got: '{actual_message}'"
        )


