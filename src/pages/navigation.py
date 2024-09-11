from playwright.sync_api import Page


class Navigation:

    def __init__(self, page: Page):
        self.page = page
        self.basket_counter = '[data-qa="header-basket-count"]'

    def get_basket_counter(self):
        self.page.locator(self.basket_counter).wait_for()
        counter = int(self.page.locator(self.basket_counter).inner_text())
        return counter
