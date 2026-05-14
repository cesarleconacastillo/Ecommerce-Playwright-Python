

class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def fill(self, selector, value):
        self.page.locator(selector).fill(value)

    def click(self, selector):
        self.page.locator(selector).click()

    def list_locator(self, selector):
        return self.page.locator(selector)

    def get_text(self, selector):
        return self.page.locator(selector).text_content()

    def get_by_placeholder(self, selector):
        self.page.get_by_placeholder(selector)

