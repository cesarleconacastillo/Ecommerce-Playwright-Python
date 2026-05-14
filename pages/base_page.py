

class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click(self, locator):
        locator.click()

    def fill(self, locator, value):
        locator.fill(value)

    def get_text(self, locator):
        return locator.text_content()


